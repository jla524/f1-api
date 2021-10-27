from flask import Blueprint

home_api = Blueprint('api', __name__)


@home_api.route('/', methods=['GET'])
def home():
    return "<h1>F1 API</h1> <p>This site is an API for Formula 1 data.</p>"
