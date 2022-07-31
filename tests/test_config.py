import tempfile
import unittest

from app.service.services import load_env_variables, get_env_file


class TestConfig(unittest.TestCase):
    """Test Config Module"""

    def setUp(self) -> None:
        """SetUp test Config"""
        self._write_env_test_file()
        file = get_env_file(self.file.name, testing=True)
        load_env_variables(file)

    def test_config_object_has_valid_values(self) -> None:
        """
        test when Config module is imported in a file
        the Class Object (not an instance) has the values
        expected from the OS environ.
        """
        from app.config.config import Config

        self.assertEqual("test_user", Config.DB_USER)
        self.assertEqual("test_password", Config.DB_PASSWORD)
        self.assertEqual("0.0.0.0", Config.DB_HOST)
        self.assertEqual("1234", Config.DB_PORT)
        self.assertEqual("example_db", Config.DB_NAME)


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
