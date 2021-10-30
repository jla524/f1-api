"""
Define test cases for helper functions
"""
from api import Config
from api.commons import helpers
from api.commons.data_routes import DataRoutes
from tests.fixture import Fixture


class TestHelpers(Fixture):
    """
    @description: test cases for helper functions
    """ 
    def test_make_dataset(self):
        """
        @description: test the make_dataset function
        """
        helpers.make_dataset()
        self.assertTrue(Config.data_dir().is_dir())

        for stem in DataRoutes().get_stems():
            file = helpers.get_file_name(stem)
            self.assertTrue(file.is_file())

    def test_get_file_name(self):
        """
        @descrirption: test the get_data_file function
        """
        for stem in DataRoutes().get_stems():
            file_name1 = helpers.get_file_name(stem)
            file_name2 = Config.data_dir() / (stem + '.csv')
            self.assertEqual(file_name1, file_name2)

        for name in ['circuit', 'driver', 'and', 'other', 'names']:
            value = helpers.get_file_name(name)
            self.assertIsNone(value)
