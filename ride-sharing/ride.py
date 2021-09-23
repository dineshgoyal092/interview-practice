class Ride:
    id =0
    def __init__(self, owner_id,origin, destination, total_seat, vehicle_id, start_time, mins):
        Ride.id += 1
        self.id = Ride.id
        self.owner_id = owner_id
        self.rider = []
        self.origin = origin
        self.destination = destination
        self.total_seat = total_seat
        self.seat_vacat = total_seat
        self.vehicle_id = vehicle_id
        self.start_time = start_time
        self.duration = mins

    def add_rider(self, id, no_seat):
        if no_seat <= self.seat_vacat:
            self.rider.append(id)
            return True
        return False

