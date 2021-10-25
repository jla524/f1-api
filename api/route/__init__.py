from flask import Flask

home_api = Flask(__name__)
home_api.config.from_object('config')
