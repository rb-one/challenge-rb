"""Microserver based on ThreadingHTTPServer"""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from .router import Router

router = Router()


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Manage GET requests"""
        data, status_code = router.process(self)
        self.make_response(data, status_code)

    def do_POST(self):
        """Manage POST requests"""
        data, status_code = router.process(self)
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
