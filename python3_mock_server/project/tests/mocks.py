"""Mock API server"""

# Standard library imports...
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re
import socket
from threading import Thread


class MockServerRequestHandler(BaseHTTPRequestHandler):
    """Placeholder"""
    USERS_PATTERN = re.compile(r'/users')
    USERS_PATTERN_ID = re.compile(r'/users/[0-9]+')

    def do_GET(self):
        """Placeholder"""
        if re.search(self.USERS_PATTERN_ID, self.path):
            # Add response status code.
            self.send_response(200)

            # Add response headers.
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()

            # Add response content.
            response_content = json.dumps([{
               'userId': 1,
               'id': 1,
               'title': 'Make the bed',
               'completed': False
            }])
            self.wfile.write(response_content.encode('utf-8'))

        elif re.search(self.USERS_PATTERN, self.path):
            # Add response status code.
            self.send_response(200)

            # Add response headers.
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()

            # Add response content.
            response_content = json.dumps([])
            self.wfile.write(response_content.encode('utf-8'))
        else:
            self.send_error(404,'File Not Found: %s' % self.path)

    def do_POST(self):
        """Placeholder"""
        self.send_error(405,'POST method not allowed: %s' % self.path)

    def do_DELETE(self):
        """Placeholder"""
        self.send_error(405,'DELETE method not allowed: %s' % self.path)

    def do_PUT(self):
        """Placeholder"""
        self.send_error(405,'UPDATE method not allowed: %s' % self.path)

    def log_message(self, format, *args):
        """Placeholder"""

def get_free_port():
    """Placeholder"""
    sock = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port

def start_mock_server(port):
    """Placeholder"""
    mock_server = HTTPServer(('localhost', port), MockServerRequestHandler)
    mock_server_thread = Thread(target=mock_server.serve_forever)
    mock_server_thread.setDaemon(True)
    mock_server_thread.start()
