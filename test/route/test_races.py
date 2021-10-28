from unittest import TestCase

from app import create_app
from api import Config
from api.commons.helpers import pull_all_data, pull_filtered_data


class TestRaces(TestCase):
    def setUp(self):
        """
        @description: return a test client
        """
        self.app = create_app().test_client()

    def test_races_all(self):
        """
        @description: test the races_all function
        """
        data = pull_all_data(Config.races_file())
        content = self.app.get('/api/v1/resources/races/all')
        self.assertEqual(data, content.get_json())

    def test_races_filter(self):
        """
        @description: test the races_filter function
        """
        file = Config.races_file()
        key = 'name'
        value = 'Monaco Grand Prix'

        data = pull_filtered_data(file, [key], {key: value})
        content = self.app.get(f'/api/v1/resources/races?{key}={value}')
        self.assertEqual(data, content.get_json())
