from flask import jsonify, request

from api import Config
from api.route.home import home_api
from api.commons.helpers import pull_all_data, pull_filtered_data


@home_api.route('/v1/resources/drivers/all', methods=['GET'])
def drivers_all():
    """
    @description: get all data from drivers.csv
    """
    data = pull_all_data(Config.drivers_file())
    return jsonify(data)


@home_api.route('/v1/resources/drivers', methods=['GET'])
def drivers_filter():
    """
    @description: get data from drivers.csv and filters by args
    """
    file = Config.drivers_file()
    columns = ['code', 'forename', 'nationality', 'number', 'surname']
    data = pull_filtered_data(file, columns, request.args)
    return jsonify(data)
