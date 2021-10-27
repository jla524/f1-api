from flask import jsonify, request

from api import Config
from api.route.home import home_api
from api.commons.helpers import pull_all_data, pull_filtered_data


@home_api.route('/v1/resources/circuits/all', methods=['GET'])
def circuits_all():
    """
    @description: get all data from circuits.csv
    """
    data = pull_all_data(Config.circuits_file())
    return jsonify(data)


@home_api.route('/v1/resources/circuits', methods=['GET'])
def circuits_filter():
    """
    @description: get data from constructors.csv and filters by args
    """
    file = Config.circuits_file()
    columns = ['name', 'location', 'country']
    data = pull_filtered_data(file, columns, request.args)
    return jsonify(data)
