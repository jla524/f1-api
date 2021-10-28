from unittest import TestCase

from app import create_app
from api import Config
from api.commons.helpers import pull_all_data, pull_filtered_data


class TestDrivers(TestCase):
    def setUp(self):
        """
        @description: return a test client
        """
        self.app = create_app().test_client()

    def test_drivers_all(self):
        """
        @description: test the drivers_all function
        """
        data = pull_all_data(Config.drivers_file())
        content = self.app.get('/api/v1/resources/drivers/all')
        self.assertEqual(data, content.get_json())

    def test_drivers_filter(self):
        """
        @description: test the drivers_filter function
        """
        file = Config.drivers_file()
        key = 'number'
        value = '33'

        data = pull_filtered_data(file, [key], {key: value})
        content = self.app.get(f'/api/v1/resources/drivers?{key}={value}')
        self.assertEqual(data, content.get_json())
