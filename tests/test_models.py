import unittest

from app.models.models import PropertyObjectModel, RealStateProperty


class TestModels(unittest.TestCase):
    """Test App MOdels"""

    def test_property_object_model_returns_list_of_dicts(self) -> None:
        """
        Test PropertyObject Model recieves a list of tuples
        and returns a list of dictionaries
        """

        self.fake_query_data = [
            ("street-0", "city-0", "state-0", "4152", "description-0"),
            ("street-1", "city-1", "state-1", "2348", "description-1"),
            ("street-2", "city-2", "state-2", "7600", "description-2"),
            ("street-3", "city-3", "state-3", "6146", "description-3"),
            ("street-4", "city-4", "state-4", "4499", "description-4"),
        ]

        model = PropertyObjectModel(RealStateProperty)
        data = model.get_data(self.fake_query_data)
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0], dict))
