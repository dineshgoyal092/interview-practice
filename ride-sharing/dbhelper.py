from selection import Selection


class RideHelper:
    users = {}
    vehicles = {}
    ride = {}
    origin_map = {}

    @staticmethod
    def add_user(user):
        if user.id not in RideHelper.users:
            RideHelper.users[user.id] = user
            return True
        return False

    @staticmethod
    def get_user( user_id):
        if user_id in RideHelper.users:
            return RideHelper.users[user_id]
        return None

    @staticmethod
    def add_vehicle( vehicle):
        if vehicle.get_vehicle_number() not in RideHelper.vehicles:
            RideHelper.vehicles[vehicle.get_vehicle_number()] = vehicle
            return True
        return False

    @staticmethod
    def get_vehicle( vehicle_number):
        if vehicle_number in RideHelper.vehicles:
            return RideHelper.vehicles[vehicle_number]
        return None

    @staticmethod
    def add_ride( ride):
        if ride.id not in RideHelper.ride:
            RideHelper.ride[ride.id] = ride
            if ride.origin in RideHelper.origin_map:
                l = RideHelper.origin_map[ride.origin]
                l.append(ride)
            else:
                RideHelper.origin_map[ride.origin] = [ride]
            return True
        return False

    @staticmethod
    def get_ride( ride_id):
        if ride_id in RideHelper.ride:
            return RideHelper.ride[ride_id]
        return False

    @staticmethod
    def select_ride( ride_id, user_id, seat):
        if ride_id in RideHelper.ride:
            RideHelper.users[user_id].add_taken_ride(ride_id)
            return RideHelper.ride[ride_id].add_rider(user_id, seat)
        return False

    @staticmethod
    def find_ride( origin, destination, proc, seat):
        for value in RideHelper.origin_map.values():
            print(value)
        for value in RideHelper.users.values():
            print(value)
        for value in RideHelper.vehicles.values():
            print(value)
        for value in RideHelper.ride.values():
            print(value)

        if origin in RideHelper.origin_map:
            all_rides = [i for i in RideHelper.origin_map[origin] if i.destination == destination and i.seat_vacat <= seat]
        else:
            return None
        if len(all_rides) < 0 :
            return None
        elif Selection.fastest ==  proc:
            min_time = all_rides[0].duration
            fastest_ride = all_rides[0]
            for ride in all_rides:
                if min_time > ride.duration:
                    min_time = ride.duration
                    fastest_ride = ride
            return fastest_ride

        elif Selection.earliest ==  proc:
            start_time = all_rides[0].start_time
            earliest_ride = all_rides[0]
            for ride in all_rides:
                if start_time > ride.start_time:
                    start_time = ride.start_time
                    earliest_ride = ride
            return earliest_ride








