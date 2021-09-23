from dbhelper import RideHelper
from selection import Gender, Selection
from user import User
from vehicle import Vehicle
from ride import Ride
from datetime import datetime

import sqlite3

db = sqlite3.connect("cab_data.db")
cursor = db.cursor()

# with open("user.txt",'r') as f:
#     f.readline()
#     for i in f:
#         print(i)
#         input = i.split()
#         name = input[0]
#         age = int(input[1])
#         gender = Gender.FEMALE
#         if input[2] == 'M':
#             gender= Gender.MALE
#         user = User(name, age, gender)
#         RideHelper.add_user(user)

select_users_table = "SELECT name,age,gender FROM  User"
for input in cursor.execute(select_users_table):
    print input
    name = input[0]
    age = int(input[1])
    gender = Gender.FEMALE
    if input[2] == 'M':
        gender= Gender.MALE
    user = User(name, age, gender)
    RideHelper.add_user(user)

with open("vehicle.txt",'r') as f:
    f.readline()
    for i in f:
        print(i)
        input = i.split()
        user_id = int(input[0])
        number = input[1]
        v_type = input[2]
        capacity = int(input[3])
        vehicle = Vehicle(v_type, number, capacity)

        user = RideHelper.get_user(user_id)
        if user:
            user.add_vehicle(vehicle.id)
            RideHelper.add_vehicle(vehicle)

with open("ride.txt",'r') as f:
    for i in f:
        print(i)
        input = i.split()
        user_id = int(input[0])
        number = input[1]
        source = input[2]
        destination = input[3]
        capacity = int(input[4])
        duration  = int(input[5])
        vehicle = RideHelper.get_vehicle(number)
        if vehicle:
            user = RideHelper.get_user(user_id)
            if user:
                ride = Ride(user_id, source, destination, capacity, vehicle.id, datetime.now(), duration)
                user.add_offer_ride(ride.id)
                RideHelper.add_ride(ride)

ride = RideHelper.find_ride('p1','p2',Selection.fastest, 2)
if ride:
    print(ride.__dict__)
else:
    print("No matching ride found")
ride = RideHelper.find_ride('p2','p1',Selection.earliest, 2)
if ride:
    print(ride.__dict__)
else:
    print("No matching ride found")




