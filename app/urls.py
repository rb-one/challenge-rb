"""App Urls"""
from . import views


URLS = [
    {
        "url": "/api/v1/properties/",
        "view": views.get_properties,
        "name": "properties"
    },
    {
        "url": "/api/v1/properties/pre-sale/",
        "view": views.get_properties_pre_sale,
        "name": "properties-pre-venta",
    },
    {
        "url": "/api/v1/properties/on-sale/",
        "view": views.get_properties_on_sale,
        "name": "properties-en-venta",
    },
    {
        "url": "/api/v1/properties/sold/",
        "view": views.get_properties_sold,
        "name": "properties-vendido",
    },
]
