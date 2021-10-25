#!/usr/bin/env python3
from json import loads

from pandas import read_csv
from flask import jsonify, request

from api.route import home_api
from api.route.not_found import page_not_found


# A route to return all of the available entries in our catelog.
@home_api.route('/api/v1/resources/drivers/all', methods=['GET'])
def api_all():
    """
    @description: pulls all data from drivers.csv
    """
    df = read_csv('data/drivers.csv')
    result = df.to_json(orient='records')
    return jsonify(loads(result))


@home_api.route('/api/v1/resources/drivers', methods=['GET'])
def api_filter():
    """
    @description: pulls data from drivers.csv and filters by various fields
    """
    df = read_csv('data/drivers.csv')
    filter_columns = ['code', 'nationality', 'number', 'surname']
    provided = False

    for column in filter_columns:
        param = request.args.get(column)
        if param:
            df = df[df[column] == param]
            provided = True

    if not provided:
        return page_not_found(404)

    results = df.to_json(orient='records')
    return jsonify(loads(results))
