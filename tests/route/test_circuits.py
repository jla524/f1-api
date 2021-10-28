from tests.fixture import Fixture


class TestCircuits(Fixture):
    _name = 'circuits'

    def test_circuits_all(self):
        """
        @description: test the circuits_all function
        """
        self.check_route_all(self._name)

    def test_circuits_filter(self):
        """
        @description: test the circuits_filter function
        """
        self.check_route_filtered(self._name, 'country', 'Italy')
