"""
Define test cases for the api/routes/blueprints.py
"""
from flask import Blueprint

from tests.fixture import Fixture
from api.routes.blueprints import make_blueprints


class TestBlueprints(Fixture):
    """
    @description: test cases for all blueprints
    """
    def test_get_blueprint(self):
        """
        @description: test the get_blueprint function for each stem
        """

    def test_make_blueprints(self):
        """
        @description: get thee make_blueprints function
        """
        for blueprint in make_blueprints():
            self.assertTrue(isinstance(blueprint, Blueprint))
