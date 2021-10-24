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
    df = read_csv('data/drivers.csv')
    result = df.to_json(orient='records')
    all_drivers = loads(result)
    return jsonify(all_drivers)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/drivers', methods=['GET'])
def api_id():
    df = read_csv('data/drivers.csv')
    filter_columns = ['code', 'nationality', 'number', 'surname']

    for column in filter_columns:
        param = request.args.get(column)
        if param:
            df = df[df[column] == param]

    results = df.to_json(orient='records')
    drivers = loads(results)
    return jsonify(drivers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
