"""Microserver based on ThreadingHTTPServer"""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Manage GET requests"""
        status_code = 200
        data = {
            "id": 1,
            "message": "Hello, World! Here is a GET response",
            "method": "GET",
        }
        self.make_response(data, status_code)

    def do_POST(self):
        """Manage POST requests"""
        status_code = 405
        data = {
            "code": "rest_method_not_allowed",
            "message": "Method Not Allowed",
            "data": {"status": 405},
        }
        self.make_response(data, status_code)

    def make_response(
        self, data: dict, status_code: int, content_type: str = "application/json"
    ) -> None:
        """
        Writes response recieves 4 paramaters
        self: the object itself
        data: A dictionary holding the data resulting from the query
        content_type: "application/json" by default
        status_code: that can be 200, 404, 405, etc
        """
        # response_code
        self.send_response(status_code)
        # create headers
        self.send_header("Content-Type", content_type)
        self.end_headers()
        # creates a json encoded representation of the dictoriary
        response = json.dumps(data).encode("utf-8")
        # writes the response
        self.wfile.write(response)


class MicroServer:
    def __init__(self):
        """init method"""

    def serve(self):
        with ThreadingHTTPServer(("localhost", 8080), RequestHandler) as server:
            print("running in http://localhost:8080/api/v1/properties")
            server.serve_forever()
