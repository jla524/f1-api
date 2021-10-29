"""
Define test cases for helper functions
"""
from api import Config
from api.commons import helpers
from tests.fixture import Fixture


class TestHelpers(Fixture):
    """
    @description: test cases for helper functions
    """
    _routes = ['circuits', 'constructors', 'drivers', 'races']

    def test_make_dataset(self):
        """
        @description: test the make_dataset function
        """
        def check_dataset_exists():
            self.assertTrue(Config.data_dir().is_dir())
            for name in self._routes:
                file = helpers.get_data_file(name)
                self.assertTrue(file.is_file())

        helpers.make_dataset()
        check_dataset_exists()

    def test_pull_all_data(self):
        """
        @description: test the pull_all_data function
        """

    def test_pull_filtered_data(self):
        """
        @description: test the pull_filtered_data function
        """

    def test_get_data_file(self):
        """
        @descrirption: test the get_data_file function
        """
        for name in self._routes:
            file_name1 = helpers.get_data_file(name)
            file_name2 = Config.data_dir() / (name + '.csv')
            self.assertEqual(file_name1, file_name2)

        for name in ['circuit', 'driver', 'and', 'other', 'names']:
            value = helpers.get_data_file(name)
            self.assertIsNone(value)
