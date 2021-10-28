from unittest import TestCase

from app import create_app
from api import Config
from api.commons.helpers import pull_all_data, pull_filtered_data


class TestCircuits(TestCase):
    def setUp(self):
        """
        @description: return a test client
        """
        self.app = create_app().test_client()

    def test_circuits_all(self):
        """
        @description: test the circuits_all function
        """
        data = pull_all_data(Config.circuits_file())
        content = self.app.get('/api/v1/resources/circuits/all')
        self.assertEqual(data, content.get_json())

    def test_circuits_filter(self):
        """
        @description: test the circuits_filter function
        """
        file = Config.circuits_file()
        key = 'country'
        value = 'Italy'

        data = pull_filtered_data(file, [key], {key: value})
        content = self.app.get(f'/api/v1/resources/circuits?{key}={value}')
        self.assertEqual(data, content.get_json())
