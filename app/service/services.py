"""App Services"""
import os

from pathlib import Path


def load_env_variables(file: str) -> None:
    """
    Function that reads a .env file and loads the content
    in OS environ
    """

    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "=" not in line:
                continue

            row = line.strip().replace("'", "").split("=")
            os.environ[row[0]] = row[1]


def get_env_file(file: str = ".env", testing=False) -> str:
    """
    Get the full path to the .env file, the default values are the following:

    - file=".env": which holds the environment variable configuration

    - testing=False: If you set True the file value will be the full path
        for the .env.test file.
    """
    file_path = Path(__file__).parent.parent.parent / file
    if testing:
        file_path = file

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            'Before start the server you have to create a ".env" file see ".env.example" file in root'
        )

    return file_path
