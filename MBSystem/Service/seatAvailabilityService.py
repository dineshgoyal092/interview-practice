class SeatAvailabilityService:
    def __init__(self):
        self.show_id = show_id
        self.available_seats = seats
        self.__status = status

    def mark_expired(self):
        self.__status = BookingStatus.Expired

    def mark_done(self):
        self.__status = BookingStatus.Executed