class User:
    id = 0
    def __init__(self, name, gender, age):
        User.id += 1
        self.__id = User.id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__ownedVehicle = []
        self.__offeredRide = []
        self.__takenRide = []


    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def add_taken_ride(self, ride_id):
        self.__takenRide.append(ride_id)

    def add_offer_ride(self, ride_id):
        self.__offeredRide.append(ride_id)

    def add_vehicle(self, vehicle_id):
        self.__offeredRide.append(vehicle_id)


