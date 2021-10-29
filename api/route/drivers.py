"""
Define content for the /api/v1/resources/drivers route
"""
from flask import Blueprint, jsonify, request

from api import Config
from api.commons.helpers import pull_all_data, pull_filtered_data

drivers = Blueprint('drivers', __name__, url_prefix=Config.drivers_route())


@drivers.route('/all', methods=['GET'])
def drivers_all():
    """
    @description: get all data from drivers.csv
    """
    data = pull_all_data(Config.drivers_file())
    return jsonify(data)


@drivers.route('/', methods=['GET'])
def drivers_filter():
    """
    @description: get data from drivers.csv and filters by args
    """
    file = Config.drivers_file()
    columns = ['code', 'forename', 'nationality', 'number', 'surname']
    data = pull_filtered_data(file, columns, request.args)
    return jsonify(data)
