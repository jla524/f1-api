"""
Create a wrapper for TestCase to help with testing the application
"""
from unittest import TestCase

from app import create_app


class Fixture(TestCase):
    """
    @description: a wrapper for TestCase with helper functions
    """
    def setUp(self):
        """
        @description: return a test client
        """
        self.app = create_app().test_client()
