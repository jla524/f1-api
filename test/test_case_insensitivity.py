from unittest import TestCase
from json import loads

from pandas import read_csv

from app import create_app
from api import Config


class TestCaseInsensitivity(TestCase):
    _file = Config.drivers_file()

    def setUp(self):
        """
        @description: return a test client
        """
        self.app = create_app().test_client()

    def pull_case_sensitive_data(self, key, value):
        """
        @description: pull data from drivers.csv and filter by value without
          altering the letter case
        """
        data = read_csv(self._file)
        data = data[data[key] == value]
        result = data.to_json(orient='records')
        return loads(result)

    def compare_data(self, key, value1, value2):
        """
        @description: check if the case sensitive filter (value1) from data
          returns the same results as the case insensitive filter (value2)
          from the api call
        """
        data = self.pull_case_sensitive_data(key, value1)
        content = self.app.get(f'/api/v1/resources/drivers?{key}={value2}')
        self.assertEqual(data, content.get_json())

    def test_uppercase(self):
        """
        @description: test to see if changing the value to uppercase gives us
          the same results
        """
        key = 'forename'
        value = 'Max'
        self.compare_data(key, value, value.upper())

    def test_lowercase(self):
        """
        @description: test to see if changing the value to lowercase gives us
          the same results
        """
        key = 'surname'
        value = 'Vettel'
        self.compare_data(key, value, value.lower())

    def test_number(self):
        """
        @description: test to see if the filter works on numerical values
        """
        key = 'number'
        value = '3'
        self.compare_data(key, value, value.upper())
        self.compare_data(key, value, value.lower())
