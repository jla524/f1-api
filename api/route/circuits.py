"""
Define content for the /api/v1/resources/circuits route
"""
from flask import Blueprint, jsonify, request

from api import Config
from api.commons.helpers import pull_all_data, pull_filtered_data

circuits = Blueprint('circuits', __name__, url_prefix=Config.circuits_route())


@circuits.route('/all', methods=['GET'])
def circuits_all():
    """
    @description: get all data from circuits.csv
    """
    data = pull_all_data(Config.circuits_file())
    return jsonify(data)


@circuits.route('', methods=['GET'])
def circuits_filter():
    """
    @description: get data from constructors.csv and filters by args
    """
    file = Config.circuits_file()
    columns = ['name', 'location', 'country']
    data = pull_filtered_data(file, columns, request.args)
    return jsonify(data)
