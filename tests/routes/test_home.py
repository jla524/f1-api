"""
Define test cases for api/routes/home.py
"""
from tests.fixture import Fixture


class TestHome(Fixture):
    """
    @description: test cases for the home route
    """
    def test_home(self):
        """
        @description: test the route screen message
        """
        response = self.app.get('/api/')
        message = "This site is an API for Formula 1 data."
        self.assertIn(message, response.get_data().decode())
