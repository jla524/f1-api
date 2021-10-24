#!/usr/bin/env python3
from json import loads
from pandas import read_csv
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>F1 API</h1> <p>This site is an API for F1 drivers.</p>"


# A route to return all of the available entries in our catelog.
@app.route('/api/v1/resources/drivers/all', methods=['GET'])
def api_all():
    """
    @description: pulls all data from drivers.csv
    """
    df = read_csv('data/drivers.csv')
    result = df.to_json(orient='records')
    return jsonify(loads(result))


@app.errorhandler(404)
def page_not_found(error):
    """
    @description: create an error page if the user encounters an error or
      inputs a route that hasn't been defined
    """
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/drivers', methods=['GET'])
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
