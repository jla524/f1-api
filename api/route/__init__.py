from flask import Flask

api = Flask(__name__)
api.config.from_object('config')
