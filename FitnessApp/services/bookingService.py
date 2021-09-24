from models.booking import Booking
from enums.bookingStatus import BookingStatus

class BookingService:
    def __init__(self, fitnessClassService, waitListService):
        self.bookings = {}
        self.fitnessClassService = fitnessClassService
        self.waitListService = waitListService

    def getBooking(self, bookingID):
        if bookingID in self.bookings:
            return self.bookings[bookingID]
        else:
            return None

    def createBooking(self, userId, classId):
        
        fitnessClass = self.fitnessClassService.getClassDetails(classId)
        newBooking = Booking(fitnessClass, userId)
        self.bookings[newBooking.id] = newBooking

        if fitnessClass.getCapacity > fitnessClass.getFilledSeats:
            fitnessClass.setFilledSeats(fitnessClass.getFilledSeats + 1)
            newBooking.setStatus(BookingStatus.Confirmed)
        else:
            self.waitListService.addIntoWaitList(classId, newBooking.id)
            newBooking.setStatus(BookingStatus.Waiting)

        return newBooking

    def cancelBooking(self, userId, bookingId):
        booking = self.getBookings[bookingId]
        if not booking:
            raise ValueError("booking doesn't exist")
        
        if booking.isConfirmed() and booking.fitnessClass.canCancel():
            booking.fitnessClass.cancel()
            booking.setStatus(BookingStatus.Cancelled)
            waitingBookingId = self.waitListService.getNextWaitListBooking(booking.fitnessClass.id)
            if waitingBookingId:
                waitingBooking = self.getBooking(waitingBookingId)
                waitingBooking.setStatus(BookingStatus.Confirmed)
                booking.fitnessClass.setFilledSeats(booking.fitnessClass.getFilledSeats + 1)
            
        elif booking.isWaitList():
            booking.fitnessClass.removeFromWaitList(userId)
            booking.setStatus(BookingStatus.Cancelled)

            
        




