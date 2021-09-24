import enum

class BookingStatus(enum.Enum):
    Active, Expired, Executed = 1, 2 ,3
import uuid
from datetime import datetime

class Booking:
    def __init__(self, show_id, seat_ids, user_id):
        self.id = uuid.uuid1()
        self.show_id = show_id
        self.seat_ids = seat_ids
        self.__status = BookingStatus.Active
        self.__user_id = user_id
        self.created_on = datetime.now()
    
    @property
    def get_status(self):
        return self.__status

    def mark_expired(self):
        self.__status = BookingStatus.Expired

    
    def mark_done(self):
        self.__status = BookingStatus.Executed