"""App Views"""


def get_properties() -> tuple[dict, int]:
    status_code = 200
    data = {
        "id": 1,
        "message": "endpoint for properties",
        "method": "GET",
    }
    return data, status_code


def get_properties_pre_sale() -> tuple[dict, int]:
    status_code = 200
    data = {
        "id": 1,
        "message": "endpoint for properties on pre-sale",
        "method": "GET",
    }
    return data, status_code


def get_properties_on_sale() -> tuple[dict, int]:
    status_code = 200
    data = {
        "id": 1,
        "message": "endpoint for properties on sale",
        "method": "GET",
    }
    return data, status_code


def get_properties_sold() -> tuple[dict, int]:
    status_code = 200
    data = {
        "id": 1,
        "message": "endpoint for properties sold",
        "method": "GET",
    }
    return (data, status_code)


def error_404_url_not_found() -> tuple[dict, int]:
    status_code = 404
    data = {
        "code": "rest_no_route",
        "message": "The requested URL does not exit",
        "data": {"status": 404},
    }

    return data, status_code


def error_405_not_allowed_method() -> tuple[dict, int]:
    status_code = 405
    data = {
        "code": "rest_method_not_allowed",
        "message": "Method Not Allowed",
        "data": {"status": 405},
    }

    return data, status_code
