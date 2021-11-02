"""
Define test cases for api/routes/blueprints.py
"""
import random

from pandas import read_csv
from flask import Blueprint

from tests.fixture import Fixture
from api.commons import helpers
from api.commons.data_routes import DataRoutes
from api.routes import blueprints


class TestBlueprints(Fixture):
    """
    @description: test cases for blueprints
    """
    def test_get_all_data(self):
        """
        @description: test the get_all_data method
        """
        for stem in DataRoutes().get_stems():
            data = blueprints.get_all_data(stem)
            self.assertIsNotNone(data)
            self.assertTrue(isinstance(data, list))

    def test_get_filtered_data(self):
        """
        @description: test the get_filtered_data method
        """
        for stem in DataRoutes().get_stems():
            file_name = helpers.get_file_name(stem)
            data1 = read_csv(file_name).astype(str)
            key = random.choice(data1.columns)
            value = data1[key].sample(n=1).values[0]

            data2 = blueprints.get_filtered_data(stem, {key: value})
            self.assertIsNotNone(data2)
            self.assertTrue(isinstance(data2, list))

    def test_get_blueprint(self):
        """
        @description: test the get_blueprint method
        """
        for stem in DataRoutes().get_stems():
            prefix = helpers.get_route(stem)
            all_route = '/'.join([prefix, 'all'])
            result = self.app.get(all_route)
            self.assertIsNotNone(result)

    def test_make_blueprints(self):
        """
        @description: test the make_blueprints method
        """
        _blueprints = blueprints.make_blueprints()
        self.assertTrue(isinstance(_blueprints, list))

        for blueprint in _blueprints:
            self.assertTrue(isinstance(blueprint, Blueprint))
