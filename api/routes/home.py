"""
Define content for the /api route
"""
from flask import Blueprint
from api import Config

home = Blueprint('home', __name__, url_prefix=Config.api_route())


@home.route('/', methods=['GET'])
def api_description() -> str:
    """
    @description: give a brief description of the API in the home page
    """
    return "<h1>F1 API</h1> <p>This site is an API for Formula 1 data.</p>"
