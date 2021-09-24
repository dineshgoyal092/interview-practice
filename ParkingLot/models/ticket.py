import uuid
from datetime import datetime
import math

class Ticket:
    
    def __init__(self, startTime, vehicleNumber, spot, vehicleType, amount= 0):
        self.__id = uuid.uuid4()
        self.startTime = startTime
        self.__vehicleNumber = vehicleNumber
        self.__spot = spot
        self.__vehicleType = vehicleType
        self.durationInHrs = 0
        self.__amount = amount
        
    def getSpot(self):
        return self.__spot
    
    def getVehicleType(self):
        return self.__vehicleType

    def getVehicleNumber(self):
        return self.__vehicleNumber
    
    def setAmount(self, amount):
        self.__amount = amount

    def getAmount(self):
        return self.__amount
    
    def setDuration(self):
        delta = datetime.now() - self.startTime
        self.durationInHrs = int(math.ceil(delta.seconds / 3600))
    