from api.route import api


@api.errorhandler(404)
def page_not_found(error):
    """
    @description: create an error page if the user encounters an error or
      inputs a route that hasn't been defined
    """
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
