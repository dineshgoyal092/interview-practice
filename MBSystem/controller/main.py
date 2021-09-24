import sys
sys.path.insert(0, '../Models')
sys.path.insert(0, '../Service')

from theater import Theater
from screen import Screen
from moviesService import MovieService
from showService import ShowService
from bookingService import BookingService
from userService import UserService
from show import Slot

def add_screen_data(theater_A, theater_B):
    s1 = Screen("S1", 10)
    s1.add_default_seats()
    theater_A.add_screen(s1)
    
    s2 = Screen("S2", 15)
    s2.add_default_seats()
    theater_A.add_screen(s2)

    a1 = Screen("A1", 10)
    a1.add_default_seats()
    theater_B.add_screen(a1)
    
    a2 = Screen("A2", 15)
    a2.add_default_seats()
    theater_B.add_screen(a2)
    


from datetime import date
import random

if __name__ == '__main__':
    theater_A = Theater("A")
    theater_B = Theater("B")
    
    add_screen_data(theater_A, theater_B)
    UserService.add_user("U1","1111111111")
    UserService.add_user("U2","1111111112")
    
    
    option = 1
    today = date.today()
    print(theater_A.__dict__)
    print(theater_B.__dict__)
    
    while(option < 7):
        option = int(input())
        if option == 1:
            print(MovieService.get_movies())
            
        elif option == 2:
            name = input()
            movie = MovieService.add_movie(name, random.randrange(60,180,15))
            screen1 = ShowService.add_show(movie, theater_A, "3:00 PM", random.randrange(100,500,50), Slot.Noon,today)
            screen2 = ShowService.add_show(movie, theater_B, "3:00 PM", random.randrange(100,500,50), Slot.Noon,today)
            print(screen1.__dict__)
            print(screen2.__dict__)
        
        elif option == 3:
            movie_id = int(input())
            list_of_shows = ShowService.get_shows(movie_id, today)
            print(list_of_shows.__dict__)
    
        elif option == 4:
            show_id = int(input())
            BookingService.close_inactive_booking(show_id)
            avail_seats = ShowService.get_seats(show_id, today)
            print(avail_seats)
            
        elif option == 5:
            seat_ids = list(map(int,input().split()))
            show_id = int(input())
            user_id = int(input())
            if ShowService.check_seats_avaialble(seat_ids, show_id):
                print(BookingService.create_booking(seat_ids, show_id, user_id))
    
    
        elif option == 6:
            booking_id = input()
            is_payment_sucess = bool(input())
            print(is_payment_sucess)
            if is_payment_sucess:
                BookingService.mark_booking_as_done(booking_id)
            else:
                BookingService.mark_booking_as_expired(booking_id)


        
        
        



    
    
    
    
    
    
    
    
    
    
    