from json import loads

from pandas import read_csv

from api import Config
from api.commons.helpers import get_data_file
from tests.fixture import Fixture


class TestCaseInsensitivity(Fixture):
    _name = 'drivers'

    def pull_case_sensitive_data(self, key, value):
        """
        @description: pull data from drivers.csv and filter by value without
          altering the letter case
        """
        file = get_data_file(self._name)
        data = read_csv(file)
        data = data[data[key] == value]
        result = data.to_json(orient=Config.orient())
        return loads(result)

    def compare_data(self, key, value1, value2):
        """
        @description: check if the case sensitive filter (value1) from data
          returns the same results as the case insensitive filter (value2)
          from the api call
        """
        data = self.pull_case_sensitive_data(key, value1)
        route = f'/api/v1/resources/{self._name}?{key}={value2}'
        content = self.app.get(route)
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
