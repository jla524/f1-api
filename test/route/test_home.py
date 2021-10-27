from unittest import TestCase

from app import create_app


class TestHome(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_home(self):
        """
        @description: test the route screen message
        """
        rv = self.app.get('/api/')
        message = "This site is an API for Formula 1 data."
        self.assertIn(message, rv.get_data().decode())
