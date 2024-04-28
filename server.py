#!/usr/bin/env python3

import http.server
import sys

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

if __name__ == '__main__':
    port = 8000  # Default port
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)
    print(f"Server running on port {port}...")
    httpd.serve_forever()
