import tempfile
import unittest
import os

from app.service.services import load_env_variables, get_env_file


class TestServices(unittest.TestCase):
    """Test App Services"""

    def setUp(self) -> None:
        """SetUp test services"""
        self._write_env_test_file()

    def test_load_env_variables(self) -> None:
        """test environment variables are loaded in OS"""
        file = get_env_file(self.file.name, testing=True)
        load_env_variables(file)

        DB_USER = os.environ.get("DB_USER")
        DB_PASSWORD = os.environ.get("DB_PASSWORD")
        DB_HOST = os.environ.get("DB_HOST")
        DB_PORT = os.environ.get("DB_PORT")
        DB_NAME = os.environ.get("DB_NAME")

        self.assertEqual("test_user", DB_USER)
        self.assertEqual("test_password", DB_PASSWORD)
        self.assertEqual("0.0.0.0", DB_HOST)
        self.assertEqual("1234", DB_PORT)
        self.assertEqual("example_db", DB_NAME)

    def test_env_file_does_not_exist(self) -> None:
        """Test .env file doest exist raise FileNotFoundError"""
        self.assertRaises(FileNotFoundError, get_env_file, "wrong_file")

    def tearDown(self) -> None:
        """Theardown method to clean up task before tests"""
        self.file.close()

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
