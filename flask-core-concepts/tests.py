from flask import Flask, jsonify, request
import unittest

app = Flask(__name__)

# Sample route for testing
@app.route('/api/v1/test', methods=['GET'])
def test():
    return jsonify({'message': 'Test passed'})

# Testing class
class MyAppTests(unittest.TestCase):
    # Setup the test client
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    # Test the test endpoint
    def test_test_endpoint(self):
        response = self.client.get('/api/v1/test')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Test passed')


if __name__ == '__main__':
    unittest.main()