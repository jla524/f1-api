from json import loads

from pandas import read_csv
from flask import jsonify

from api.route.not_found import page_not_found


def pull_all_data(file):
    """
    @description: pull all data from file
    """
    df = read_csv(file)
    result = df.to_json(orient='records')
    return jsonify(loads(result))


def pull_filtered_data(file, columns, parameters):
    """
    @description: pull data from file and filter by parameters
    """
    df = read_csv(file)
    param_match = False

    for column in columns:
        param = parameters.get(column)
        if param:
            df = df[df[column] == param]
            param_match = True

    if not param_match:
        return page_not_found(404)

    results = df.to_json(orient='records')
    return jsonify(loads(results))
