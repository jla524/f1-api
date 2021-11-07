"""
Define test cases for the package
"""
from unittest import TestCase

from api import Config


class TestPackage(TestCase):
    """
    @description: test cases for the package
    """
    def test_package_name(self):
        """
        @description: test the package name
        """
        self.assertEqual(Config.package(), 'api')

    def test_default_env(self):
        """
        @description: test the default env
        """
        self.assertEqual(Config.default_env(), 'dev')
