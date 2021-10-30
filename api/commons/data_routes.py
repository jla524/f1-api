"""
Define a class to hold names of data files and routes
"""
from api import Config


def read_data_files():
    """
    @description: get a list of file path from data_dir
    """
    data_files = Config.data_dir().iterdir()
    return list(data_files)


class DataRoutes:
    """
    @description: hold names of data files and rooutes
    """
    def __init__(self):
        self.__data_files = read_data_files()
        self.__stems = self.__make_stems()
        self.__file_map = self.__make_file_map()
        self.__route_map = self.__make_route_map()

    def __make_stems(self):
        """
        @description: get the list of file names without the extension
        """
        stems = [file_name.stem for file_name in self.__data_files]
        return stems

    def __make_file_map(self):
        """
        @description: make a map of file name using filess from data_dir
        """
        file_map = {}

        for data_file, stem in zip(self.__data_files, self.__stems):
            file_map[stem] = data_file

        return file_map

    def __make_route_map(self):
        """
        @description: make a map of route names based on the resources route
        """
        route_map = {}

        for stem in self.__stems:
            route_map[stem] = '/'.join([Config.resources_route(), stem])

        return route_map

    def get_data_files(self):
        """
        @description: getter for the list of data files
        """
        return self.__data_files

    def get_stems(self):
        """
        @description: getter for the list of stems
        """
        return self.__stems

    def get_file_map(self):
        """
        @description: getter for the file map
        """
        return self.__file_map

    def get_route_map(self):
        """
        @description: getter for the route map
        """
        return self.__route_map
