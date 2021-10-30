"""
Define content for the /api/v1/resources/circuits route
"""
from json import loads

from pandas import read_csv
from flask import Blueprint, jsonify, request

from api import Config
from api.commons import helpers
from api.routes.not_found import page_not_found
from api.commons.data_routes import DataRoutes


def get_all_data(stem):
    """
    @description: pull all data from file
    """
    data = read_csv(helpers.get_file_name(stem))
    result = data.to_json(orient=Config.orient())
    return loads(result)


def get_filtered_data(stem, parameters):
    """
    @description: read data from file and filter by parameters
    """
    data = read_csv(helpers.get_file_name(stem))
    param_match = False

    for column in data.columns:
        param = parameters.get(column)
        if param:
            data = data[data[column] == param]
            param_match = True

    if not param_match:
        return page_not_found()

    results = data.to_json(orient=Config.orient())
    return loads(results)


def get_blueprint(stem):
    """
    @description: create a blueprint from the given stem
    """
    blueprint = Blueprint(stem, __name__, url_prefix=helpers.get_route(stem))

    @blueprint.route('/all', methods=['GET'])
    def get_all():
        """
        @description: get all data from stem
        """
        data = get_all_data(stem)
        return jsonify(data)

    @blueprint.route('', methods=['GET'])
    def get_filter():
        """
        @description: get data from stem and filters by args
        """
        data = get_filtered_data(stem, request.args)
        return jsonify(data)

    return blueprint


def make_blueprints():
    """
    @description: get a list of blueprints
    """
    stems = DataRoutes().get_stems()
    blueprints = [get_blueprint(stem) for stem in stems]
    return blueprints
