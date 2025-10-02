"""
Task 2-5:
A simple HTTP server to test ApacheBench (ab) performance.
This server responds with a plain text message to any GET request.
To test the server, you can use ApacheBench (ab) from the command line:
ab -n 100 -c 10 http://127.0.0.1:8080/
"""
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    """A simple HTTP request handler that responds with a plain text message."""
    def get_request(self):
        """Handle GET requests."""
        # Set response status code
        self.send_response(200)
        # Set response headers
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        # Send response body
        self.wfile.write(b"Hello, ApacheBench!")

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080
    server = HTTPServer((host, port), SimpleHandler)
    print(f"Starting HTTP server on {host}:{port}...")
    server.serve_forever()



