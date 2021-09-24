class Movie:
    id= 0 
    def __init__(self, name, mins):
        Movie.id += 1
        self.id = Movie.id
        self.__name = name
        self.duration = mins

    def get_name(self):
        return self.__name
