from flask import jsonify, request

from api import Config
from api.route.home import home_api
from api.commons.helpers import pull_all_data, pull_filtered_data


@home_api.route('/api/v1/resources/races/all', methods=['GET'])
def races_all():
    """
    @description: get all data from races.csv
    """
    data = pull_all_data(Config.races_file())
    return jsonify(data)


@home_api.route('/api/v1/resources/races', methods=['GET'])
def races_filter():
    """
    @description: get data from races.csv and filters by args
    """
    file = Config.races_file()
    columns = ['year', 'name', 'date']
    data = pull_filtered_data(file, columns, request.args)
    return jsonify(data)
