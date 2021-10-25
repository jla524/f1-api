from api.route import home_api


@home_api.route('/', methods=['GET'])
def home():
    return "<h1>F1 API</h1> <p>This site is an API for F1 drivers.</p>"
