"""App Router"""

class Router:
    """
    Process the incomming http requests filtering by invalid and
    valid requests, if its valid search in valid urls to match a
    view with its url.
    """

    def __init__(self):
        pass

    def process(self, request) -> tuple[dict, int]:
        """Parse the route using the path from RequestHandler"""
        if request.command == "POST":
            return Router.process_invalid_requests(request)

        return Router.process_valid_request(request)

    @staticmethod
    def process_invalid_requests(request) -> callable:
        """Process an invalid request"""
        if request.command == "POST":
            status_code = 405
            data = {
                "code": "rest_method_not_allowed",
                "message": "Method Not Allowed",
                "data": {"status": 405},
            }
            
            return data, status_code

    @staticmethod
    def process_valid_request(request) -> callable:
        """
        Process a valid request with GET method and a valid URL
        and returns the view that matches the URL
        """
        status_code = 200
        data = {
            "id": 1,
            "message": "Hello, World! Here is a GET response",
            "method": "GET",
        }
        return data, status_code
