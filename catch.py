#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from sys import argv


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-length'])
        post_data = self.rfile.read(content_length)
        print(post_data.decode('utf-8'))
        self._set_response()


def run(server_class=HTTPServer, handler_class=S, port=8080):
    try:
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
    except OSError:
        print(f"Port {port} is unavailable")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
