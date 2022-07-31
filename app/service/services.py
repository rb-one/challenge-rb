"""App Services"""
import os

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
