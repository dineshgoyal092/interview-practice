class User:
    id = 0
    def __init__(self, name, phone):
        User.id += 1
        self.id = User.id
        self.__name = name
        self.__phone  = phone

    def get_name(self):
        return self.__name
