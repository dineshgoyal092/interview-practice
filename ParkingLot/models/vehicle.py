from abc import ABC, abstractmethod
from enums.vehicleType import VehicleType


class Vehicle(ABC):
    def __init__(self, vehicleNumber, vehcileType):
        self.vehicleNumber = vehicleNumber
        self.vehicleType = vehcileType
        self.ticket = None

    def assignTicket(self, ticket):
        self.ticket = ticket

    def releaseTicket(self):
        self.ticket = None


class TwoWheeler(Vehicle):
    def __init__(self, vehcileNumber):
        super().__init__(vehcileNumber, VehicleType.TwoWheeler)

class FourWheeler(Vehicle):
    def __init__(self, vehcileNumber):
        super().__init__(vehcileNumber, VehicleType.FourWheeler)
