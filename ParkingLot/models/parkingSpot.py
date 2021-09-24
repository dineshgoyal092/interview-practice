from abc import ABC, abstractmethod
from enums.spotType import SpotType

class ParkingSpot(ABC):
    def __init__(self, spotType, spotNumber):
        self.spotType = spotType
        self.spotNumber = spotNumber
        self.vehicle = None

    def parkVehicle(self, vehicle):
        self.vehicle = vehicle

    def unParkVehicle(self):
        self.vehicle = None

class TwoWheelerSpot(ParkingSpot):
    def __init__(self, spotNumber):
        super().__init__(SpotType.Small, spotNumber)


class FourWheelerSpot(ParkingSpot):
    def __init__(self, spotNumber):
        super().__init__(SpotType.Medium, spotNumber)