from abc import ABC, abstractmethod
from enums.spotType import SpotType
from models.parkingSpot import TwoWheelerSpot, FourWheelerSpot

class ParkingSpotService(ABC):
    def __init__(self):
        self.spots = {}
        self.__freeSpots = 0
        self.availableSpots = []

    @abstractmethod
    def createSpot(self):
        pass

    def printSpot(self):
        print("printing all spots")
        print(self.spots)

    def addSpot(self, spotNumber):
        spot = self.createSpot(spotNumber)
        self.spots[spotNumber] = spot
        self.__freeSpots += 1
        self.availableSpots.append(spotNumber)

    def getSpot(self):
        if self.__freeSpots > 0:
            self.__freeSpots -= 1
            spotNumber = self.availableSpots.pop()
            return self.spots[spotNumber]
    
    def unPark(self, spot):
        self.__freeSpots += 1
        self.availableSpots.append(spot.spotNumber)
        

class SmallParkingService(ParkingSpotService):
    def __init__(self):
        super().__init__()

    def createSpot(self, spotNumber):
        spot = TwoWheelerSpot(spotNumber)
        return spot


class MediumParkingService(ParkingSpotService):
    def __init__(self):
        super().__init__()

    def createSpot(self, spotNumber):
        spot = FourWheelerSpot(spotNumber)
        return spot



        # vignesh.n@udaan.com