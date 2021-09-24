import sys
sys.path.insert(0,"../Models")

from booking import Booking, BookingStatus
from showService import ShowService
# from userService import UserService

class BookingService:
    bookings = []

    @staticmethod
    def create_booking(seat_ids, show_id, user_id):
        booking = Booking(show_id,seat_ids, user_id)
        BookingService.add_booking(booking)
        ShowService.lock_seats(seat_ids, show_id)
        # UserService.start_user_session(user_id,booking.id)
        return booking.id

    @staticmethod
    def add_booking(booking):
        BookingService.bookings.append(booking)

    # @staticmethod
    # def get_unavailable_seats(show_id):
    #     for i in BookingService.bookings:
    #         if i.show_id == show_id and i.status != BookingStatus.Expired:
    #             i.unavailable_seats.append(i.seats)

    @staticmethod
    def mark_booking_as_done(booking_id):
        print(booking_id)
        for i in BookingService.bookings:
            print(i.__dict__)
            if i.id == booking_id and i.get_status == BookingStatus.Active:
                print("found booking", booking_id)
                i.mark_done()
                # UserService.delete_session(i.user_id)
                if ShowService.book_seats(i.seat_ids, i.show_id):
                    return True
        return None

    @staticmethod
    def mark_booking_as_expired(booking_id):
        for i in BookingService.bookings:
            if i.id == booking_id and i.get_status == BookingStatus.Active:
                i.mark_expired()
                # UserService.delete_session(i.user_id)
                if ShowService.release_seats(i.seat_ids, i.show_id):
                    return True
        return None


    @staticmethod
    def mark_booking_as_closed(booking):
        if booking.get_status == BookingStatus.Active:
            booking.mark_expired()
            # UserService.delete_session(i.user_id)
            if ShowService.release_seats(booking.seat_ids, booking.show_id):
                return True
        return None


    @staticmethod
    def close_inactive_booking(show_id):
        import datetime
        timeout = datetime.timedelta(seconds= 60)
        import time
        print("start")
        time.sleep(30)
        print("end")
        for i in BookingService.bookings:
            print("booking", i.__dict__)
            if i.show_id == show_id:
                print("inactive_booking", i.__dict__)
                if i.created_on + timeout < datetime.datetime.now():
                    BookingService.mark_booking_as_closed(i)
                return True
        return None
                
                
                
        
                
    
    

