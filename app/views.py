"""App Views"""
from app.database.queries import all_properties, pre_sale_properties, on_sale_properties, sold_properties
from app.models.models import RealStateProperty
from app.service.services import QueryCommand


command = QueryCommand(RealStateProperty)


def get_properties(request) -> tuple[dict, int]:
    '''returns all the available properties'''
    data = command.process_query(all_properties, request.query_params)
    status_code = 200
    # for future development work, a try/catch can be
    # implemented if something goes wrong and send another
    # status code in all the views
    return data, status_code


def get_properties_pre_sale(request) -> tuple[dict, int]:
    '''returns all the available properties on pre-sale status'''
    data = command.process_query(all_properties, request.query_params)
    status_code = 200
    return data, status_code


def get_properties_on_sale(request) -> tuple[dict, int]:
    '''returns all the available properties on on-sale status'''
    data = command.process_query(all_properties, request.query_params)
    status_code = 200
    return data, status_code


def get_properties_sold(request) -> tuple[dict, int]:
    '''returns all the available properties on sold status'''
    data = command.process_query(all_properties, request.query_params)
    status_code = 200
    return (data, status_code)


def error_404_url_not_found(request) -> tuple[dict, int]:
    '''returns 404 status for not existing urls'''
    status_code = 404
    data = {
        "code": "rest_no_route",
        "message": "The requested URL does not exit",
        "data": {"status": 404},
    }

    return data, status_code


def error_405_not_allowed_method(request) -> tuple[dict, int]:
    '''returns 405 status for not allowed method POST'''
    status_code = 405
    data = {
        "code": "rest_method_not_allowed",
        "message": "Method Not Allowed",
        "data": {"status": 405},
    }

    return data, status_code
