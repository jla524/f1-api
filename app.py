"""
Create and run the Flask app
"""
from flask import app, Flask

from api.routes.home import home
from api.data.make_dataset import download_data
from api.routes.blueprints import make_blueprints


def create_api() -> app.Flask:
    """
    @description: create the Flask api
    """
    download_data()

    api = Flask(__name__)
    api.config.from_object('config')
    api.register_blueprint(home)

    for blueprint in make_blueprints():
        api.register_blueprint(blueprint)

    return api


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-H', '--host', default='0.0.0.0',
                        type=str, help='the interface to bind to')
    parser.add_argument('-p', '--port', default=5000,
                        type=int, help='the port to bind to')

    args = parser.parse_args()
    host = args.host
    port = args.port

    f1_api = create_api()
    f1_api.run(host=host, port=port)
