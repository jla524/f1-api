from unittest import TestCase

from app import create_app
from api import Config
from api.commons.helpers import pull_all_data, pull_filtered_data


class TestConstructors(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_constructors_all(self):
        """
        @description: test the constructors_all function
        """
        data = pull_all_data(Config.constructors_file())
        content = self.app.get('/api/v1/resources/constructors/all')
        self.assertEqual(data, content.get_json())

    def test_constructors_filter(self):
        """
        @description: test the constructors_filter function
        """
        file = Config.constructors_file()
        key = 'name'
        value = 'McLaren'

        data = pull_filtered_data(file, [key], {key: value})
        content = self.app.get(f'/api/v1/resources/constructors?{key}={value}')
        self.assertEqual(data, content.get_json())
