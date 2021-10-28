from tests.fixture import Fixture


class TestHome(Fixture):

    def test_home(self):
        """
        @description: test the route screen message
        """
        rv = self.app.get('/api/')
        message = "This site is an API for Formula 1 data."
        self.assertIn(message, rv.get_data().decode())
