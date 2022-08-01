import unittest
from threading import Thread
import json
import requests

from app.server.microserver import MicroServer


class TestMicroServer(unittest.TestCase):
    """Test the Basic Usage of MicroServer"""

    def setUp(self) -> None:
        """SetUp test starts the server as daemon"""
        server = MicroServer()
        self.mock_server_thread = Thread(target=server.serve, daemon=True)
        self.mock_server_thread.start()

    def test_handler_do_get_sucessfull(self) -> None:
        """test a valid url using GET method"""
        res = requests.get("http://localhost:8080/api/v1/properties/")
        data = json.loads(res.text)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.headers["Content-type"], "application/json")
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0], dict))
        
    def test_handler_can_not_do_post_405_error(self) -> None:
        """test a valid url but using POST method which is not allowed"""
        res = requests.post("http://localhost:8080/api/v1/properties/")
        self.assertEqual(res.status_code, 405)
        self.assertEqual(res.headers["Content-type"], "application/json")
        self.assertEqual(res.json()["message"], "Method Not Allowed")

    def tearDown(self) -> None:
        """
        Theardown method for future reference, the thread daemon is automatically killed
        when the test finish.
        """
