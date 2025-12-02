#!/usr/bin/python3
"""A simple API server using http.server"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        """Helper method to send JSON response"""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def _send_text(self, text, status=200):
        """Helper method to send plain text response"""
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(text.encode("utf-8"))

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/":
            self._send_text("Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(data)
        elif self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self._send_json(info)
        elif self.path == "/status":
            self._send_text("OK")
        else:
            self._send_text("Endpoint not found", status=404)


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Run the API server on port 8000"""
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server on http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
