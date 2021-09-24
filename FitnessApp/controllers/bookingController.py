from services.bookingService import BookingService

class BookingController:
    def __init__(self, fitnessClassService, waitListService):
        self.bookingService = BookingService(fitnessClassService, waitListService)
    
    def addBooking(self, userId, classId):
        return self.bookingService.createBooking(userId, classId)
        

    def cancelBooking(self, userId, bookingId):
        return self.bookingService.cancelBooking(userId, bookingId)
        