import os
import sys
import importlib
import subprocess
import threading

from utils import HandlerFactory, ThreadingSimpleServer

def run():
    '''
        Selenium based html pages tester
        Usage: html_checker [URL_GITHUB_SUBDIRECTORY]
        Example: html_checker https://github.com/atefMck/holbertonschool-web_front_end/tree/master/0x06-responsive_design
    '''
    if len(sys.argv) <= 1:
        print('html_checker: wrong number of arguments')
        print('Usage: html_checker [URL_GITHUB_SUBDIRECTORY]')
        print('Example: html_checker https://github.com/atefMck/holbertonschool-web_front_end/tree/master/0x06-responsive_design')
        exit(1)
    
    PORT = 7000
    REPO_FOLDER_LINK = sys.argv[1]
    FOLDER_NAME = REPO_FOLDER_LINK[::-1].split('/')[0][::-1]
    SERVE_PATH = os.path.join('/app/', FOLDER_NAME, '')
    test_suite_source = '/app/test_suites/'+ FOLDER_NAME + '/test.py'
    if os.path.exists(test_suite_source):
        test = importlib.import_module('test_suites.{}.test'.format(FOLDER_NAME))
    else:
        print('Error: Test suite for project {} doesn\'t exist'.format(FOLDER_NAME))
        exit(2)
    
    repo_source = '/app/'+ FOLDER_NAME
    if not os.path.exists(repo_source):
        print('Downloading directory..')
        subprocess.run(["gitdir", REPO_FOLDER_LINK], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print('Repository directory successfully downloaded')
    
    handler = HandlerFactory(SERVE_PATH)
    server = ThreadingSimpleServer(('localhost', PORT), handler)
    t = threading.Thread(target=server.serve_forever)
    t.start()
    try:
        test.run_test()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run()