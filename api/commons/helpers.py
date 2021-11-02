"""
Define helper functions
"""
from pathlib import Path

from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

from api import Config
from api.commons.data_routes import DataRoutes


def make_dataset() -> None:
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


def get_file_name(stem) -> Path:
    """
    @description: getter for a specific data file
    """
    return DataRoutes().get_file_map().get(stem)


def get_route(stem) -> str:
    """
    @description: getter for a specific route name
    """
    return DataRoutes().get_route_map().get(stem)
