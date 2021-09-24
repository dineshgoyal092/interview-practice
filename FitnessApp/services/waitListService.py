from models.waitList import WaitList

class WaitListService:
    def __init__(self):
        self.waitLists = {}

    def addIntoWaitList(self, fitnessClassId, bookingId):
        if fitnessClassId in self.waitLists:
            self.waitLists[fitnessClassId].append(bookingId)
        else:
            self.waitLists[fitnessClassId] = [bookingId]

    def getNextWaitListBooking(self, fitnessClassId):
        if fitnessClassId in self.waitLists:
            return self.waitLists[fitnessClassId].pop(0)
        return None