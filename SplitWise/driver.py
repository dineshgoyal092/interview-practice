from controllers.billController import BillController
from controllers.userController import UserController
from services.userService import UserService
from services.billService import BillService


billController = BillController(BillService())
userController = UserController(UserService())

u = userController.addUser("Dinesh")
print(u.__dict__)

with open("users.txt",'r') as f:
    f.readline()
    for i in f:
        print(i)
        input = i.split()
        name = str(input[1])
        user = userController.addUser(name)
        print(user.__dict__)

import flask
from flask import Flask, jsonify, abort, make_response
app = flask.Flask(__name__)
app.config["DEBUG"] = True
import requests

@app.route('/add_user/', methods=['POST'])
def addUser():
    print(request.json)
    if not request.json or not 'name' in request.json:
        abort(400)
    name = request.json['name']
    print("create_user")
    u = userController.addUser(name)
    print(u)
    data = {'user_id': u.id}
    return data, 201




if __name__ == "__main__":
    app.run()
    response = requests.post('http://127.0.0.1:5000/add_user/', json = {'name':"user_name"})
    
    if response.status_code == 400:
         print ({"error":"while uploading data"}, 400)
    
    print(response.json())

    