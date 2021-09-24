import sys
sys.path.insert(0, '../Models')

from movie import Movie

class MovieService:
    movies = []

    @staticmethod
    def add_movie(name, duration_in_mins):
        for i in MovieService.movies:
            if i.get_name() == name:
                return i
        movie = Movie(name, duration_in_mins)
        MovieService.movies.append(movie)
        return movie
    
    @staticmethod
    def get_movies():
        # list_of_movies = []
        # for i in self.__movies:
        #     if i.date == date:
        #         list_of_movies.append(i)
        # return list_of_movies
        list_of_movies = []
        for i in MovieService.movies:
            list_of_movies.append({"name":i.get_name(), "duraiton": i.duration})
        return list_of_movies
