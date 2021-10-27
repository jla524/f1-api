from unittest import TestCase
from json import loads

from pandas import read_csv

from app import create_app
from api import Config


class TestDrivers(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_drivers_all(self):
        """
        @description: test the drivers_all function
        """
        df = read_csv(Config.drivers_file())
        result = df.to_json(orient='records')

        rv = self.app.get('/api/v1/resources/drivers/all')
        self.assertEqual(loads(result), rv.get_json())

    def test_drivers_filter(self):
        """
        @description: test the drivers_filter function
        """
        df = read_csv(Config.drivers_file())
        df = df[df['number'] == '33']
        result = df.to_json(orient='records')

        rv = self.app.get('/api/v1/resources/drivers?number=33')
        self.assertEqual(loads(result), rv.get_json())
