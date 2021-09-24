import unittest
import requests

class SimpleTest1(unittest.TestCase):

    # Returns True or False.
    def test_create_user(self):
        print("running_test_create_user")
        response = requests.post('http://127.0.0.1:5000/create_user/', json = {'name':"user_name",'phone':"phone"})
        assert response.status_code == 201

    def test_create_theater(self):
        print("running_test_create_theater")
        response = requests.post('http://127.0.0.1:5000/add_theater/', json = {'name':"AA"})
        assert response.status_code == 200

    def test_create_theater(self):
        print("running_test_create_theater")
        response = requests.post('http://127.0.0.1:5000/add_theater/', json = {'name':"AA"})
        # assert response.status_code == 200
        theater_id = response.json()['theater_id']
        print(theater_id)
        assert theater_id > 0

if __name__ == '__main__':
    unittest.main()