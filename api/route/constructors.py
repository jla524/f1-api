from flask import request

from api import Config
from api.route.home import home_api
from api.commons.helpers import pull_all_data, pull_filtered_data


@home_api.route('/v1/resources/constructors/all', methods=['GET'])
def constructors_all():
    """
    @description: get all data from constructors.csv
    """
    return pull_all_data(Config.constructors_file())


@home_api.route('/v1/resources/constructors', methods=['GET'])
def constructors_filter():
    """
    @description: get data from constructors.csv and filters by args
    """
    file = Config.constructors_file()
    columns = ['name', 'nationality']
    return pull_filtered_data(file, columns, request.args)
