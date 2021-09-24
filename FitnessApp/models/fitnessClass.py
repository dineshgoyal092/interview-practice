import uuid
from enums.fitnessType import FitnessType
from datetime import datetime
class FitnessClass:
    def __init__(self, name, startTime, durationInMins, fitnessType, capacity):
        self.__id = uuid.uuid1()
        self.__name = name
        self.__startTime = startTime
        self.__durationInMins = durationInMins
        self.__fitnessType = fitnessType
        self.__capacity = capacity
        self.__filledSeats = 0
    
    @property
    def getId(self):
        return self.__id
        
    @property
    def getFilledSeats(self):
        return self.__filledSeats

    @property
    def getCapacity(self):
        return self.__capacity
    
    
    def canCancel(self):
        now = datetime.now()
        classStartTime = datetime.timdeself.__startTime
        delta = classStartTime - now
        
        if delta.minutes > 30:
            return True
        else:
            return False
    
    def cancel(self):
        self.__filledSeats -= 1
    
    
        
