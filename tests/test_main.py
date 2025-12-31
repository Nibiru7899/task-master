# Import necessary libraries
import unittest
from src.main import app

# Define a test class for the main application
class TestMain(unittest.TestCase):
    def test_home_page(self):
        # Create a test client for the application
        tester = app.test_client()
        # Send a GET request to the home page
        response = tester.get('/')
        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)

# Run the tests
if __name__ == '__main__':
    unittest.main()