"""App Services"""
from ast import If
import os

from pathlib import Path


from app.config.config import Config
from app.database.database import DatabaseDriver, Queryhole
from app.models.models import PropertyObjectModel, RealStateProperty


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


class QueryCommand:
    def __init__(self, model):
        """init method"""
        # Load db Config
        load_env_variables(get_env_file())
        config = Config()
        # setup driver
        db_driver = DatabaseDriver(config)
        self.qh = Queryhole(db_driver)
        # create model
        self.model = PropertyObjectModel(model)

    def process_query(self, query, query_params=None):
        """
        Recieves a query string, calls the queryhole instance
        and pass the result to the model that returns a list
        of dictionaries
        """
        if query_params:
            query += self.parse_query_params(query_params)

     
        query = self.qh.make_query(query)
        data = self.model.get_data(query)
        return data

    def parse_query_params(self, query_params):
        cleaned_params = []
        params = query_params.split("&")

        for param in params:
            param = param.split("=")
            param_name = param[0].lower()
            param_value = param[1].replace("%20", " ")

            if param_name == "ciudad":
                cleaned_params.append(f" AND p.city='{param_value}'")

            if param_name == "annio-construccion":
                cleaned_params.append(f" AND p.year={int(param_value)}")

            if param_name == "estado":
                cleaned_params.append(f" AND s.name='{param_value}'")


        return "\n".join(cleaned_params)
