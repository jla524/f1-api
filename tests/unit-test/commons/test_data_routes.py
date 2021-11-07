"""
Define test cases for api/commons/data_routes.py
"""
from pathlib import Path

from tests.fixture import Fixture
from api import Config
from api.commons.data_routes import DataRoutes


class TestDataRoutes(Fixture):
    """
    @description: test cases for data routes
    """
    def test_get_data_files(self):
        """
        @descriptions: test the get_data_files method
        """
        data_files = DataRoutes().get_data_files()
        self.assertTrue(isinstance(data_files, list))

        for data_file in data_files:
            self.assertTrue(data_file.is_file())

    def test_get_stems(self):
        """
        @description: test the get_stems method
        """
        stems = DataRoutes().get_stems()
        self.assertTrue(isinstance(stems, list))

        for stem in stems:
            self.assertTrue(isinstance(stem, str))
            data_file = Config.data_dir() / (stem + '.csv')
            self.assertTrue(isinstance(data_file, Path))
            self.assertTrue(data_file.is_file())

    def test_get_file_map(self):
        """
        @description: test the get_file_map method
        """
        file_map = DataRoutes().get_file_map()
        self.assertTrue(isinstance(file_map, dict))
        stems = DataRoutes().get_stems()

        for stem in stems:
            data_file = file_map.get(stem)
            self.assertIsNotNone(data_file)
            self.assertTrue(isinstance(data_file, Path))
            self.assertTrue(data_file.is_file())

    def test_get_route_map(self):
        """
        @description: test the gt_rooute_map method
        """
        route_map = DataRoutes().get_route_map()
        self.assertTrue(isinstance(route_map, dict))
        stems = DataRoutes().get_stems()

        for stem in stems:
            route = route_map.get(stem)
            self.assertIsNotNone(route)
            self.assertTrue(isinstance(route, str))
