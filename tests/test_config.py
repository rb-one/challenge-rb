import tempfile
import unittest

from app.service.services import load_env_variables, get_env_file
from app.config.config import Config

class TestConfig(unittest.TestCase):
    """Test Config Module"""

    def setUp(self) -> None:
        """SetUp test Config"""
        self._write_env_test_file()
        file = get_env_file(self.file.name, testing=True)
        load_env_variables(file)
        self.config = Config()

    def test_config_object_has_valid_values(self) -> None:
        """
        test that config Instance have the values of OS environ
        """
        self.assertEqual("test_user",  self.config.DB_USER)
        self.assertEqual("test_password",  self.config.DB_PASSWORD)
        self.assertEqual("0.0.0.0",  self.config.DB_HOST)
        self.assertEqual("1234",  self.config.DB_PORT)
        self.assertEqual("example_db",  self.config.DB_NAME)


    def tearDown(self) -> None:
        """Theardown method to clean up task before tests"""
        self.file.close()
        # environment variables are removed before test automatically

    # auxiliar function to setUp test
    def _write_env_test_file(self) -> None:
        """Writes a temporal .env for testing"""
        self.test_db_data = [
            b"DB_USER='test_user'\n",
            b"DB_PASSWORD='test_password'\n",
            b"# t# this is a coment, blank lines are allowed too\n",
            b"\n",
            b"DB_HOST='0.0.0.0'\n",
            b"DB_PORT=1234\n",
            b"DB_NAME='example_db'\n",
        ]

        self.file = tempfile.NamedTemporaryFile(prefix=".env.test_", dir="./tests/")
        for data in self.test_db_data:
            self.file.write(data)

        self.file.seek(0)
