"""
Define functions to make dataset
"""
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

from api import Config


def download_data() -> None:
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
