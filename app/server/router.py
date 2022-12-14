"""App Router"""
from app.urls import URLS
from app.views import error_404_url_not_found, error_405_not_allowed_method


class Router:
    """
    Process the incomming http requests filtering by invalid and
    valid requests, if its valid search in valid urls to match a
    view with its url.
    """

    def __init__(self):
        self.valid_urls = [attrs["url"] for attrs in URLS]

    def process(self, request) -> tuple[dict, int]:
        """Parse the route using the path from RequestHandler"""
        request = Router.parse_request_path(request)

        if request.command == "POST" or request.path not in self.valid_urls:
            return Router.process_invalid_requests(request)

        return Router.process_valid_request(request)

    @staticmethod
    def parse_request_path(request):
        path = request.path.split("?")
        request.path = path[0]
        request.query_params = None

        if len(path) > 1:
            request.query_params = path[1]

        return request

    @staticmethod
    def process_invalid_requests(request) -> callable:
        """Process an invalid request"""
        if request.command == "POST":
            return error_405_not_allowed_method(request)

        return error_404_url_not_found(request)

    @staticmethod
    def process_valid_request(request) -> callable:
        """
        Process a valid request with GET method and a valid URL
        and returns the view that matches the URL
        """
        for url in URLS:
            if request.path == url["url"]:
                return url["view"](request)
