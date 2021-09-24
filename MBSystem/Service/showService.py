import sys
sys.path.insert(0, '../Models')

from show import Show
from theaterService import TheaterService

class ShowService:
    shows = []
    
    @staticmethod
    def available_screen(date, theater_id, slot):
        theater = TheaterService.get_theater_by_id(theater_id)
        print(theater)
        screens = theater.get_screens
        for j in screens:
            flag = False
            for i in ShowService.shows:
                if i.screen_id == j.id and i.date == date and i.slot == slot:
                    flag = True
                    continue
            if not flag:
                return j
        return None

    @staticmethod
    def add_show(movie_id, theater_id, start_time, price, slot, date):
        screen = ShowService.available_screen(date, theater_id, slot)
        if screen:
            show = Show(movie_id, start_time, price, screen, slot, date, theater_id)
            ShowService.shows.append(show)
            return show
        else:
            return None

    @staticmethod
    def get_movie_shows(movie_id, date, theater_id, slot):
        list_of_shows = []
        for i in ShowService.shows:
            if i.movie_id == movie_id:
                list_of_shows.append(i)
        if date:
            list_of_shows = filter(lambda x: x.date == date, list_of_shows)
        if theater_id:
            list_of_shows = filter(lambda x: x.theater_id == theater_id, list_of_shows)
        if slot:
            list_of_shows = filter(lambda x: x.slot == slot, list_of_shows)
        
        res = []
        for i in list_of_shows:
            res.append({'show_id': i.id, 'scrren_id': i.screen_id, 'theater_id': i.theater_id, 'slot': i.slot, 'date': i.date})
        return res

    @staticmethod
    def get_seats(show_id):
        for i in ShowService.shows:
            if i.id == show_id:
                return i.available_seats
        return []
    

    @staticmethod
    def check_seats_avaialble(seat_ids, show_id):
        for i in ShowService.shows:
            if i.id == show_id:
                return set(seat_ids) <= set(i.available_seats)
        return None

    @staticmethod
    def lock_seats(seat_ids, show_id):
        for i in ShowService.shows:
            if i.id == show_id:
                i.available_seats = list(set(i.available_seats) - set(seat_ids))
                i.locked_seats += seat_ids
        return

    @staticmethod
    def release_seats(seat_ids, show_id):
        for i in ShowService.shows:
            if i.id == show_id:
                i.available_seats += seat_ids
                print(i.locked_seats, seat_ids)
                i.locked_seats = list(set(i.locked_seats) - set(seat_ids))
                return True
        return False

    @staticmethod
    def book_seats(seat_ids, show_id):
        for i in ShowService.shows:
            if i.id == show_id:
                print("match shows", i.__dict__)
                i.available_seats = list(set(i.available_seats) - set(seat_ids))
                i.booked_seats += seat_ids
                return True
        return False

    @staticmethod
    def get_packed_shows(theater_id):
        packed_shows = []
        for i in ShowService.shows:
            if not theater_id:
                packed_shows.append( {"movie_id": i.movie_id, "theater_id": i.theater_id, "screen_id": i.screen_id, "slot": i.slot})
            elif i.theater_id == theater_id:
                packed_shows.append( {"movie_id": i.movie_id, "theater_id": i.theater_id, "screen_id": i.screen_id, "slot": i.slot})
        return packed_shows

    @staticmethod
    def get_available_shows(theater_id):
        slots = TheaterService.get_slots(theater_id)
        print("slots", slots)
        packed_shows = ShowService.get_packed_shows(theater_id)
        print("packed_shows", packed_shows)
        for i in slots:
            for j in packed_shows:
                if j['screen_id'] == i['screen_id']:
                    i['slots'].remove(j['slot'])
        return slots


    
