"""
Define helper functions
"""
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

from api import Config
from api.commons.data_routes import DataRoutes


def make_dataset():
    """
    @description: download the F1 dataset if it is not in the data/ directory
    """
    data_dir = Config.data_dir()

    if data_dir.is_dir():
        return

    url = 'http://ergast.com/downloads/f1db_csv.zip'
    with urlopen(url) as response:
        with ZipFile(BytesIO(response.read())) as zip_file:
            zip_file.extractall(data_dir)


def get_file_name(name):
    """
    @description: getter for a specific data file
    """
    return DataRoutes().get_file_map().get(name)


def get_route(name):
    """
    @description: getter for a specific route name
    """
    return DataRoutes().get_route_map().get(name)
