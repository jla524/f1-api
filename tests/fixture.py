from unittest import TestCase

from app import create_app
from api.commons import helpers


class Fixture(TestCase):
    def setUp(self):
        """
        @description: return a test client
        """
        self.app = create_app().test_client()

    def check_route_all(self, name):
        """
        @description: given a route name, check to see if the content in the
          corresponding data file matches with the content from the API
        """
        file = helpers.get_data_file(name)
        data = helpers.pull_all_data(file)
        content = self.app.get(f'/api/v1/resources/{name}/all')
        self.assertEqual(data, content.get_json())

    def check_route_filtered(self, name, key, value):
        """
        @description: given a route name, check to see if the filtered content
          in the corresponding data file matches with the content from the API
        """
        file = helpers.get_data_file(name)
        data = helpers.pull_filtered_data(file, [key], {key: value})
        content = self.app.get(f'/api/v1/resources/{name}?{key}={value}')
        self.assertEqual(data, content.get_json())
