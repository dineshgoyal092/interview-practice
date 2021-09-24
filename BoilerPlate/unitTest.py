import unittest
import requests

class SimpleTest(unittest.TestCase):

    # Returns True or False.
    def test_case(self):
        print("running_test_case")
        a = 3
        b = 2
        assert a+b == 5
        
    def testHealthApi(self):
        response = requests.get('http://127.0.0.1:5000/health')
        assert response.status_code == 400


if __name__ == '__main__':
    unittest.main()