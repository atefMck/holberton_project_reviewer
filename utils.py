from http.server import HTTPServer, SimpleHTTPRequestHandler 
from socketserver import ThreadingMixIn

def HandlerFactory(serve_path):
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=serve_path, **kwargs)
        
        def log_message(self, format, *args):
            return
    return Handler

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass