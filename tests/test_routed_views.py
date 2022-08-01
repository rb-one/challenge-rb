import json
import unittest
from threading import Thread

import requests

from app.server.microserver import MicroServer


class TestViews(unittest.TestCase):
    """
    Test Microservice can serve the individual endpoints
    using views.pyn urls.py and router.py
    """

    def setUp(self) -> None:
        """SetUp test starts the server as daemon"""
        server = MicroServer()
        self.mock_server_thread = Thread(target=server.serve, daemon=True)
        self.mock_server_thread.start()

    def test_get_properties(self) -> None:
        """test a valid url using GET method"""
        res = requests.get("http://localhost:8080/api/v1/properties/")
        data = json.loads(res.text)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers["Content-type"], "application/json")
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0], dict))

    def test_get_properties_pre_sale(self) -> None:
        """test a valid url using GET method"""
        res = requests.get("http://localhost:8080/api/v1/properties/pre-sale/")
        data = json.loads(res.text)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers["Content-type"], "application/json")
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0], dict))

    def test_get_properties_on_sale(self) -> None:
        """test a valid url using GET method"""
        res = requests.get("http://localhost:8080/api/v1/properties/on-sale/")
        data = json.loads(res.text)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers["Content-type"], "application/json")
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0], dict))

    def test_get_properties_sold(self) -> None:
        """test a valid url using GET method"""
        res = requests.get("http://localhost:8080/api/v1/properties/sold/")
        data = json.loads(res.text)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers["Content-type"], "application/json")
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0], dict))

    def test_error_404_url_not_found(self) -> None:
        """test an unvalid url using GET method"""
        res = requests.get("http://localhost:8080/api/v1/whatever")
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.headers["Content-type"], "application/json")
        self.assertEqual(res.json()["message"], "The requested URL does not exit")

    def test_error_405_not_allowed_method(self) -> None:
        """test a valid url but using POST method which is not allowed"""
        res = requests.post("http://localhost:8080/api/v1/properties")
        self.assertEqual(res.status_code, 405)
        self.assertEqual(res.headers["Content-type"], "application/json")
        self.assertEqual(res.json()["message"], "Method Not Allowed")

    def tearDown(self) -> None:
        """
        Theardown method for future reference, the thread daemon is automatically killed
        when the test finish.
        """
