"""
Create and run the Flask app
"""
from flask import Flask

from api.routes.home import home
from api.routes.blueprints import make_blueprints
from api.commons.helpers import make_dataset


def create_app():
    """
    @description: create the Flask app
    """
    app = Flask(__name__)
    app.config.from_object('config')
    make_dataset()

    app.register_blueprint(home)

    for blueprint in make_blueprints():
        app.register_blueprint(blueprint)

    return app


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

    my_app = create_app()
    my_app.run(host=host, port=port)
