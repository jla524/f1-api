"""
Define functions to test api/data/make_dataset
"""
from shutil import rmtree

from api import Config
from api.commons import helpers
from api.commons.data_routes import DataRoutes
from api.data.make_dataset import download_data
from tests.fixture import Fixture


class TestMakeDataset(Fixture):
    """
    @description: test functions in make_dataset
    """
    def unlink_data_dir(self):
        """
        @description: remove the data directory
        """
        data_dir = Config.data_dir()

        if data_dir.is_dir():
            rmtree(data_dir)

        self.assertFalse(Config.data_dir().exists())

    def test_download_data(self):
        """
        @description: test the make_dataset function
        """
        self.unlink_data_dir()
        download_data()
        self.assertTrue(Config.data_dir().is_dir())

        for stem in DataRoutes().get_stems():
            file = helpers.get_file_name(stem)
            self.assertTrue(file.is_file())
