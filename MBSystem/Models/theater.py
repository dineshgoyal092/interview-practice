import json

from screen import Screen
class Theater:
    id = 0
    
    def __init__(self, name):
        Theater.id += 1
        self.id = Theater.id
        self.__name = name
        self.__screens = []

    @property
    def get_name(self):
        return self.__name
        
    def add_screen(self, screen):
        self.__screens.append(screen)

    @property
    def get_screens(self):
        return self.__screens

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    def get_screen_by_id(self, id):
        for i in self.__screens:
            if i.id == id:
                return i
        return None

    def get_or_create_screen_by_name(self, name, no_of_seats):
        for i in self.__screens:
            if i.get_name().lower() == name.lower():
                return i
        s = Screen(name, no_of_seats)
        s.add_default_seats()
        self.add_screen(s)
        return s