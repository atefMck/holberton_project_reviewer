import os
import sys
import importlib

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading

PORT = 8000
FOLDER_NAME = sys.argv[1]
SERVE_PATH = os.path.join('/app/test_suites/', FOLDER_NAME, '')
test = importlib.import_module('test_suites.{}.test'.format(FOLDER_NAME))

class Handler(BaseHTTPRequestHandler):
    pass

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    server = ThreadingSimpleServer(('0.0.0.0', 4444), Handler)
    t = threading.Thread(target=server.serve_forever)
    t.start()
    server.shutdown()
    server.server_close()


if __name__ == '__main__':
    run()