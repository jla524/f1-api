from flask import request

from api import Config
from api.route import api
from api.commons.helpers import pull_all_data, pull_filtered_data


@api.route('/api/v1/resources/races/all', methods=['GET'])
def races_all():
    """
    @description: get all data from races.csv
    """
    return pull_all_data(Config.races_file())


@api.route('/api/v1/resources/races', methods=['GET'])
def races_filter():
    """
    @description: get data from races.csv and filters by args
    """
    file = Config.races_file()
    columns = ['year', 'name', 'date']
    return pull_filtered_data(file, columns, request.args)
