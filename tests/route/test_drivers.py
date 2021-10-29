"""
Define test cases for the /api/v1/resources/drivers route
"""
from tests.fixture import Fixture


class TestDrivers(Fixture):
    """
    @description: test cases for the drivers route
    """
    _name = 'drivers'

    def test_drivers_all(self):
        """
        @description: test the drivers_all function
        """
        self.check_route_all(self._name)

    def test_drivers_filter(self):
        """
        @description: test the drivers_filter function
        """
        self.check_route_filtered(self._name, 'number', '33')
