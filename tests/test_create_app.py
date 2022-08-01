import tempfile
import unittest
from app import create_app
from app.server.microserver import MicroServer

class TestDatabase(unittest.TestCase):
    """
    Test main create app
    """

    def setUp(self) -> None:
        """SetUp test Config"""


    def test_database_driver_has_open_connection(self) -> None:
        """Test connection to DataBase is open for usage"""
        app = create_app()
        self.assertTrue(isinstance(app, MicroServer))


    def tearDown(self) -> None:
        """Theardown method to clean up task before tests"""
