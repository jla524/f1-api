from json import loads

from pandas import read_csv

from api import Config
from api.route.not_found import page_not_found


def pull_all_data(file):
    """
    @description: pull all data from file
    """
    data = read_csv(file)
    result = data.to_json(orient=Config.orient())
    return loads(result)


def pull_filtered_data(file, columns, parameters):
    """
    @description: pull data from file and filter by parameters
    """
    data = read_csv(file)
    param_match = False

    for column in columns:
        param = parameters.get(column)
        if param:
            data = data[data[column].str.lower() == param.lower()]
            param_match = True

    if not param_match:
        return page_not_found(404)

    results = data.to_json(orient=Config.orient())
    return loads(results)


def get_data_file(name):
    file_map = {
        'circuits': Config.circuits_file(),
        'constructors': Config.constructors_file(),
        'drivers': Config.drivers_file(),
        'races': Config.races_file()
    }
    return file_map.get(name)
