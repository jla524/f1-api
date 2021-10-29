"""
Define content for the /api/v1/resources/races/all route
"""
from flask import Blueprint, jsonify, request

from api import Config
from api.commons.helpers import pull_all_data, pull_filtered_data

races = Blueprint('races', __name__, url_prefix=Config.races_route())


@races.route('/all', methods=['GET'])
def races_all():
    """
    @description: get all data from races.csv
    """
    data = pull_all_data(Config.races_file())
    return jsonify(data)


@races.route('', methods=['GET'])
def races_filter():
    """
    @description: get data from races.csv and filters by args
    """
    file = Config.races_file()
    columns = ['year', 'name', 'date']
    data = pull_filtered_data(file, columns, request.args)
    return jsonify(data)
