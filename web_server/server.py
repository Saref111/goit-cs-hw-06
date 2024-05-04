import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import os
import socket

SOCKET_SERVER_ADDRESS = ('localhost', 5000)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.copyfile(f, self.wfile)
        elif parsed_path.path.endswith('.html'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(parsed_path.path[1:], 'rb') as f:
                self.copyfile(f, self.wfile)
        elif parsed_path.path.endswith(('.css', '.png')):
            self.send_response(200)
            if parsed_path.path.endswith('.css'):
                self.send_header('Content-type', 'text/css')
            elif parsed_path.path.endswith('.png'):
                self.send_header('Content-type', 'image/png')
            self.end_headers()
            with open(parsed_path.path[1:], 'rb') as f:
                self.copyfile(f, self.wfile)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('error.html', 'rb') as f:
                self.copyfile(f, self.wfile)
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_post_data = parse_qs(post_data)
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(SOCKET_SERVER_ADDRESS)
            client_socket.sendall(post_data.encode())

with socketserver.TCPServer(("", 3000), CustomHandler) as httpd:
    print("HTTP server is running at port 3000")
    httpd.serve_forever()
