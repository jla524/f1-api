"""
Create and run the Flask app
"""
from flask import Flask

from api.route.circuits import circuits
from api.route.constructors import constructors
from api.route.drivers import drivers
from api.route.home import home
from api.route.races import races
from api.commons.helpers import make_dataset


def create_app():
    """
    @description: create the Flask app
    """
    app = Flask(__name__)
    app.config.from_object('config')

    app.register_blueprint(home)
    app.register_blueprint(circuits)
    app.register_blueprint(constructors)
    app.register_blueprint(drivers)
    app.register_blueprint(races)

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000,
                        type=int, help='port to listen on')

    args = parser.parse_args()
    port = args.port

    make_dataset()
    my_app = create_app()
    my_app.run(host='0.0.0.0', port=port)
