#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cross-Origin-Resource-Policy", "cross-origin")
        super().end_headers()

    def log_message(self, *a): pass  # silence logs

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("Serving at http://localhost:8765  —  http://192.168.178.183:8765")
HTTPServer(("", 8765), Handler).serve_forever()
