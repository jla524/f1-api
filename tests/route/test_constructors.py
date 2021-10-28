from tests.fixture import Fixture


class TestConstructors(Fixture):
    _name = 'constructors'

    def test_constructors_all(self):
        """
        @description: test the constructors_all function
        """
        self.check_route_all(self._name)

    def test_constructors_filter(self):
        """
        @description: test the constructors_filter function
        """
        self.check_route_filtered(self._name, 'name', 'McLaren')
