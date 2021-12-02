import os
import sys
import importlib
import subprocess

from http.server import HTTPServer, SimpleHTTPRequestHandler 
from socketserver import ThreadingMixIn
import threading

PORT = 7000
REPO_FOLDER_LINK = sys.argv[1]
FOLDER_NAME = REPO_FOLDER_LINK[::-1].split('/')[0][::-1]
SERVE_PATH = os.path.join('/app/', FOLDER_NAME, '')
test = importlib.import_module('test_suites.{}.test'.format(FOLDER_NAME))

print('Downloading directory..')
subprocess.run(["gitdir", REPO_FOLDER_LINK], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
print('Repository directory successfully downloaded')

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SERVE_PATH, **kwargs)
    
    def log_message(self, format, *args):
        return


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    server = ThreadingSimpleServer(('localhost', PORT), Handler)
    t = threading.Thread(target=server.serve_forever)
    t.start()
    try:
        test.run_test()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run()