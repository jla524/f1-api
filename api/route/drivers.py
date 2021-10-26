#!/usr/bin/env python3
from flask import request

from api import Config
from api.route import home_api
from api.commons.helpers import pull_all_data, pull_filtered_data


@home_api.route('/api/v1/resources/drivers/all', methods=['GET'])
def api_all():
    """
    @description: get all data from drivers.csv
    """
    return pull_all_data(Config.drivers_file())


@home_api.route('/api/v1/resources/drivers', methods=['GET'])
def api_filter():
    """
    @description: get data from drivers.csv and filters by args
    """
    columns = ['code', 'nationality', 'number', 'surname']
    return pull_filtered_data(Config.drivers_file(), columns, request.args)
