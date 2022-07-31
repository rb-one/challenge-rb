from dataclasses import dataclass


@dataclass
class RealStateProperty:
    direction: str
    ciudad: str
    state: str
    sale_price: str
    Description: str


class PropertyObjectModel:
    def __init__(self, model):
        self.model = model

    def get_data(self, query) -> list[dict]:
        """
        Returns a list of Dictionaries comming from
        parse the result from  QueryHold.make_query method
        """
        data = [
            RealStateProperty(data[0], data[1], data[2], data[3], data[4]).__dict__
            for data in query
        ]

        return data
