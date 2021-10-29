"""
Define content for the /api/v1/resources/constructors/all route
"""
from flask import Blueprint, jsonify, request

from api import Config
from api.commons.helpers import pull_all_data, pull_filtered_data

constructors = Blueprint('constructors', __name__,
                         url_prefix=Config.constructors_route())


@constructors.route('/all', methods=['GET'])
def constructors_all():
    """
    @description: get all data from constructors.csv
    """
    data = pull_all_data(Config.constructors_file())
    return jsonify(data)


@constructors.route('/', methods=['GET'])
def constructors_filter():
    """
    @description: get data from constructors.csv and filters by args
    """
    file = Config.constructors_file()
    columns = ['name', 'nationality']
    data = pull_filtered_data(file, columns, request.args)
    return jsonify(data)
