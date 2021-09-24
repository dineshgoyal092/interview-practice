from seat import Seat
from show import Slot

class Screen:
    id = 0
    def __init__(self, name, no_of_seats):
        Screen.id += 1
        self.id = Screen.id
        self.__name = name
        self.__no_of_seats = no_of_seats
        self.__seats = []
        self.slots = [Slot.Morning, Slot.Noon, Slot.Evening, Slot.Night]

    def get_name(self):
        return self.__name

    def add_seat(self, seat):
        self.__seats.append(seat)
        
    # def set_no_of_seats(self, seat):
    # 
    @property    
    def get_screen_seats(self):
        return [i.id for i in self.__seats]
        
    def add_default_seats(self):
        for i in range(self.__no_of_seats):
            seat = Seat((i / 6) + 1, (i % 6) + 1)
            self.__seats.append(seat) 