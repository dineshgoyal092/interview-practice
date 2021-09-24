import enum

class Slot(str, enum.Enum):
    Morning, Noon, Evening, Night = 'morning', 'noon', 'evening', 'night'
    
class Show:
    id = 0
    def __init__(self, movie_id, start_time, price, screen, slot, date, theater_id):
        Show.id += 1
        self.id = Show.id 
        self.movie_id = movie_id
        self.__start_time = start_time
        self.__price = price
        self.screen_id = screen.id
        self.slot = slot
        self.date = date
        self.available_seats = screen.get_screen_seats
        self.theater_id = theater_id
        self.locked_seats = []
        self.booked_seats = []
    
    