import uuid
from enums.bookingStatus import BookingStatus

class Booking:
    def __init__(self, fitnessClass, user, status= BookingStatus.Pending):
        self.id = uuid.uuid1()
        self.__fitnessClass = fitnessClass
        self.__user = user
        self.__status = status

    def setStatus(self, status):
        self.__status = status
    
    def isWaitList(self):
        return self.__status == BookingStatus.WaitList
    
    def isConfirmed(self):
        return self.__status == BookingStatus.Confirmed