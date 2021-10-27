from flask import Flask
from api.route.home import home_api
from api.route import circuits, constructors, drivers, races


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(home_api, url_prefix='/api')
    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000,
                        type=int, help='port to listen on')

    args = parser.parse_args()
    port = args.port

    app = create_app()
    app.run(host='0.0.0.0', port=port)
