import sys
sys.path.insert(0, '../Models')

from theater import Theater

class TheaterService:
    theaters = []

    @staticmethod
    def add_or_get_theater(name):
        for i in TheaterService.theaters:
            if i.get_name.lower() == name.lower():
                return i
        theater = Theater(name)
        TheaterService.theaters.append(theater)
        return theater

    @staticmethod
    def get_theater_by_id(id):
        for i in TheaterService.theaters:
            if i.id == id:
                return i
        return None

    @staticmethod
    def add_screen(id, name, no_of_seats):
        for i in TheaterService.theaters:
            if i.id == id:
                print(i.__dict__)
                s = i.get_or_create_screen_by_name(name, no_of_seats)
                return s
        return None

    @staticmethod
    def get_slots(id):
        slots = []
        for i in TheaterService.theaters:
            for screen in i.get_screens:
                if not id:
                    slots.append({"theater_id":i.id, "screen_id": screen.id, "slots":screen.slots.copy()})
                elif i.id == id:
                        slots.append({"theater_id":i.id, "screen_id": screen.id, "slots":screen.slots.copy()})
        return slots
