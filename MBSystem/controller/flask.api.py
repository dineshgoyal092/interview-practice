import flask
from flask import Flask, jsonify, request, abort, make_response

import sys
sys.path.insert(0, '../Models')
sys.path.insert(0, '../Service')
sys.path.insert(0, '../files')
from theater import Theater
from screen import Screen
from moviesService import MovieService
from theaterService import TheaterService
from showService import ShowService
from bookingService import BookingService
from userService import UserService
from show import Slot
import json
from json import JSONEncoder
from datetime import date
from lockService import LockGroup

app = flask.Flask(__name__)
app.config["DEBUG"] = True
import requests
import random

# subclass JSONEncoder
class CustomEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

@app.route('/upload_data/', methods=['GET'])
def uploadData():
    print("start_uploading")
    with open("../files/user.txt",'r') as f:
        f.readline()
        for i in f:
            input = i.split(',')
            print(input)
            user_name = input[0]
            phone = input[1]
            response = requests.post('http://127.0.0.1:5000/create_user/', json = {'name':user_name,'phone':phone})

            if response.status_code == 400:
                return {"error":"while uploading data"}, 400
            print(response.json())

    response = requests.post('http://127.0.0.1:5000/add_theater/', json = {'name':'AA'})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())
    theater_id1= response.json()['theater_id']

    response = requests.post('http://127.0.0.1:5000/add_theater/', json = {'name':'BB'})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())

    theater_id2= response.json()['theater_id']

    response = requests.post('http://127.0.0.1:5000/add_screen/', json = {'name':'S1', "theater_id": theater_id1, "no_of_seats":random.randrange(5,10,1)})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())

    screen_id1= response.json()['screen_id']

    response = requests.post('http://127.0.0.1:5000/add_screen/', json = {'name':'S2', "theater_id": theater_id1, "no_of_seats":random.randrange(5,10,1)})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())
    
    screen_id2= response.json()['screen_id']

    response = requests.post('http://127.0.0.1:5000/add_screen/', json = {'name':'S3', "theater_id": theater_id2, "no_of_seats":random.randrange(5,10,1)})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())
    
    screen_id3= response.json()['screen_id']


    response = requests.post('http://127.0.0.1:5000/add_movie/', json = {'name':'M1', "duration":random.randrange(100,200,10)})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())

    movie_id1= response.json()['movie_id']

    response = requests.post('http://127.0.0.1:5000/add_movie/', json = {'name':'M2', "duration":random.randrange(100,200,10)})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())

    movie_id2= response.json()['movie_id']


    response = requests.post('http://127.0.0.1:5000/add_show/', json = {    "movie_id":movie_id1,
                                                                            "theater_id": theater_id1,
                                                                            "slot": "morning",
                                                                            "date":"2021-06-15",
                                                                            "price":random.randrange(200,500,50),
                                                                            "start_time":"09:00"})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())

    show_id_1= response.json()['show_id']

    response = requests.post('http://127.0.0.1:5000/add_show/', json = {    "movie_id":movie_id2,
                                                                            "theater_id": theater_id2,
                                                                            "slot": "morning",
                                                                            "date":"2021-06-15",
                                                                            "price":random.randrange(200,500,50),
                                                                            "start_time":"09:00"})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())

    show_id_1= response.json()['show_id']

    response = requests.post('http://127.0.0.1:5000/add_show/', json = {    "movie_id":movie_id1,
                                                                            "theater_id": theater_id2,
                                                                            "slot": "evening",
                                                                            "date":"2021-06-15",
                                                                            "price":random.randrange(200,500,50),
                                                                            "start_time":"09:00"})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())

    show_id_1= response.json()['show_id']

    response = requests.post('http://127.0.0.1:5000/add_show/', json = {    "movie_id":movie_id2,
                                                                            "theater_id": theater_id1,
                                                                            "slot": "noon",
                                                                            "date":"2021-06-15",
                                                                            "price":random.randrange(200,500,50),
                                                                            "start_time":"09:00"})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())

    show_id_1= response.json()['show_id']


    response = requests.post('http://127.0.0.1:5000/add_show/', json = {    "movie_id":movie_id2,
                                                                            "theater_id": theater_id1,
                                                                            "slot": "noon",
                                                                            "date":"2021-06-15",
                                                                            "price":random.randrange(200,500,50),
                                                                            "start_time":"09:00"})

    if response.status_code == 400:
        return {"error":"while uploading data"}, 400
    print(response.json())

    show_id_1= response.json()['show_id']



    data = {"success": True}
    return data, 200

@app.route('/create_user/', methods=['POST'])
def createUser():
    print(request.json)
    if not request.json or not 'name' in request.json or not 'phone' in request.json:
        abort(400)
    name = request.json['name']
    phone = request.json['phone']
    print("create_user")
    u = UserService.add_user(name,phone)
    print(u)
    data = {'user_id': u.id}
    return data, 201


@app.route('/add_theater/', methods=['POST'])
def addTheater():
    if not request.json or not 'name' in request.json:
        abort(400)
    name = request.json['name']
    t = TheaterService.add_or_get_theater(name)
    # t = CustomEncoder().encode(t)
    # print(t)
    data = {'theater_id': t.id}
    return data, 200


@app.route('/add_screen/', methods=['POST'])
def addScreen():
    if not request.json or not 'theater_id' in request.json or not 'name' in request.json or not 'no_of_seats' in request.json:
        abort(400)
    theater_id = request.json['theater_id']
    screen_name = request.json['name']
    no_of_seats = request.json['no_of_seats']
    s = TheaterService.add_screen(theater_id, screen_name, no_of_seats)
    if s:
        data = {'theater_id': theater_id, "screen_id": s.id}
        return data, 201
    else:
        data = {'error': 'theater id not valid'}
        return data, 400


@app.route('/add_movie/', methods=['POST'])
def addMovie():
    if not request.json or not 'name' in request.json or not 'duration' in request.json:
        abort(400)
    movie_name = request.json['name']
    duration_in_mins = request.json['duration']
    print(movie_name)
    m = MovieService.add_movie(movie_name, duration_in_mins)
    if m:
        data = {'movie_id': m.id}
        return data, 201
    else:
        data = {'error': 'movie name not valid'}
        return data, 400


@app.route('/get_movies/', methods=['GET'])
def getMovies():
    if not request.json:
        abort(400)
    movies = MovieService.get_movies()
    print(movies)
    if movies == None:
        data = {'error': 'movie name not valid'}
        return data, 400
    if len(movies) > 0:
        return {"data": movies}, 200
    else:
        data = {'error': 'No movie exist'}
        return data, 200

@app.route('/get_shows/', methods= ['POST'])
def getShows():
    # if not request.json:
    #     abort(400)
    theater_id = request.json.get('theater_id')
    packed_shows = ShowService.get_packed_shows(theater_id)
    print("packed_shows", packed_shows)
    available_slots = ShowService.get_available_shows(theater_id)
    
    print("available_slots", available_slots)
    data = {"packed_shows": packed_shows, "available_slots": available_slots}
    return data, 200
    

@app.route('/add_show/', methods=['POST'])
def addShow():
    if not request.json or not 'movie_id' in request.json or not 'theater_id' in request.json or not 'slot' in request.json or not 'date' in request.json:
        abort(400)
    movie_id = request.json['movie_id']
    theater_id = request.json['theater_id']
    slot = request.json['slot']
    date = request.json['date']
    import datetime
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    print(date_time_obj)
    start_time = request.json['start_time']
    price = request.json['price']
    try:
        slot = Slot(slot)
    except:
        abort(400)
    show = ShowService.add_show(movie_id, theater_id, start_time, price,slot, date)
    print(show)
    if show:
        data = {'show_id': show.id, "scrren_id": show.screen_id}
        return data, 201
    else:
        data = {'error': 'Non available screen'}
        return data, 400

@app.route('/movie_show/', methods=['POST'])
def movieShow():
    if not request.json or not 'movie_id' in request.json:
        abort(400)
    movie_id = request.json['movie_id']
    theater_id = request.json.get('theater_id')
    slot = request.json.get('slot')
    date = request.json.get('date')
    try:
        if slot: 
            slot = Slot(slot)
    except:
        abort(400)
    shows = ShowService.get_movie_shows(movie_id, date, theater_id, slot)
    print(shows)
    data = {"data": shows}
    return data, 200

@app.route('/get_seats/', methods=['POST'])
def getSeats():
    if not request.json or not 'show_id' in request.json:
        abort(400)
    show_id = request.json['show_id']
    date = request.json.get('date')
    import datetime
    if date:
        date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        print(date_time_obj.date())
        date= date_time_obj.date()
    else:
        date = datetime.date.today()
    import threading
    t1 = threading.Thread(target=BookingService.close_inactive_booking, args=(show_id,))
    t1.start()
    # BookingService.close_inactive_booking(show_id)
    avail_seats = ShowService.get_seats(show_id)
    print(avail_seats)
    data = {"data": avail_seats}
    return data, 200


@app.route('/lock_seats/', methods=['POST'])
def lockSeats():
    if not request.json or not 'show_id' in request.json or not 'seat_ids' in request.json:
        abort(400)
    show_id = request.json['show_id']
    seat_ids = request.json['seat_ids']
    user_id = request.json['user_id']
    lock= LockGroup.get_lock(show_id)
    lock.acquire(blocking=True, timeout=90)
    print("lock_aquired", show_id)
    import time
    if ShowService.check_seats_avaialble(seat_ids, show_id):
        booking_id = BookingService.create_booking(seat_ids, show_id, user_id)
        data = {"booking_id": booking_id}
        lock.release()
        return data, 200
    else:
        data = {'error': 'seats not avialbale'}
        return data, 400


@app.route('/payment/', methods=['POST'])
def bookSeats():
    if not request.json or not 'status' in request.json or not 'payment_token' in request.json:
        abort(400)
    status = request.json['status']
    booking_id = request.json['booking_id']
    token = request.json['payment_token']
    import uuid
    booking_id = uuid.UUID(booking_id)
    if status:
        status = BookingService.mark_booking_as_done(booking_id)
    else:
        status = BookingService.mark_booking_as_expired(booking_id)
    if status:
        data = {"success": status}
        return data, 200
    else:
        data = {'error': 'seats not avialbale'}
        return data, 400

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)

