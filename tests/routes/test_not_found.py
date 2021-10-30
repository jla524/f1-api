"""
Define test cases for api/routes/not_found.py
"""
from tests.fixture import Fixture


class TestNotFound(Fixture):
    """
    @description: test cases for the 404 page
    """
    def test_404(self):
        """
        @description: test the 404 message
        """
        message = "<h1>404</h1><p>The resource could not be found.</p>"
        response = self.app.get('/api/v1/resources/drivers?id=1')
        self.assertIn(message, response.get_data().decode())
