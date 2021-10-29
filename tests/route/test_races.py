"""
Define test cases for the /api/v1/resources/races route
"""
from tests.fixture import Fixture


class TestRaces(Fixture):
    """
    @descriptioon: test cases for the races route
    """
    _name = 'races'

    def test_races_all(self):
        """
        @description: test the races_all function
        """
        self.check_route_all(self._name)

    def test_races_filter(self):
        """
        @description: test the races_filter function
        """
        self.check_route_filtered(self._name, 'name', 'Monaco Grand Prix')
