import tempfile
import unittest

from app.config.config import Config
from app.service.services import load_env_variables, get_env_file
from app.database.database import DatabaseDriver, Queryhole


class TestDatabase(unittest.TestCase):
    """
    Test Config Module
    
    For the pourpose of this excercise I need to test the
    the DatabaseDriver and QueryHold objects againt the provided 
    database (prod for me), for real a development process the best 
    is to have a "development database" in a running docker container if
    I have the time I will try it
    """

    def setUp(self) -> None:
        """SetUp test Config"""
        file = get_env_file()
        load_env_variables(file)
        self.config = Config()

    def test_database_driver_has_open_connection(self) -> None:
        """Test connection to DataBase is open for usage"""
        db_driver = DatabaseDriver(self.config)
        connection = db_driver.get_connection()
        self.assertTrue(connection.is_connected())
        connection.close()

    def test_database_driver_connection_is_closed_after_opened(self):
        """Test connection to DataBase is closed after using it"""
        db_driver = DatabaseDriver(self.config)
        connection = db_driver.get_connection()
        db_driver.close_connection()

        self.assertTrue(connection.is_closed())

    def test_queryhole_retrives_data(self) -> None:
        '''
        Test Queryhole can get data from dabatabse, the pourpose of this
        is verify that a row exists as the repository is public, and I want
        to keep as anonymous as posible the tipics related with the schema
        '''
        db_driver = DatabaseDriver(self.config)
        q = Queryhole(db_driver)
        quiery = f"SELECT * FROM {self.config.DB_NAME}.status_history limit 1"
        row = q.make_query(quiery)
        self.assertTrue(row)

    def tearDown(self) -> None:
        """Theardown method to clean up task before tests"""
