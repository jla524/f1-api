"""
Create and run the Flask app
"""
from argparse import ArgumentParser

from flask import Flask

from api.routes.home import home
from api.routes.blueprints import make_blueprints
from api.data.make_dataset import download_data


def create_app():
    """
    @description: create the Flask app
    """
    app = Flask(__name__)
    app.config.from_object('config')
    download_data()

    app.register_blueprint(home)

    for blueprint in make_blueprints():
        app.register_blueprint(blueprint)

    return app


def run():
    """
    @description: run the app with specified host and port
    """
    parser = ArgumentParser()
    parser.add_argument('-H', '--host', default='0.0.0.0',
                        type=str, help='the interface to bind to')
    parser.add_argument('-p', '--port', default=5000,
                        type=int, help='the port to bind to')

    args = parser.parse_args()
    host = args.host
    port = args.port

    my_app = create_app()
    my_app.run(host=host, port=port)


if __name__ == '__main__':
    run()
