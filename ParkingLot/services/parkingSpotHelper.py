# from . import parkingSpotService
from .parkingSpotService import SmallParkingService, MediumParkingService
from models.parkingSpot import ParkingSpot, TwoWheelerSpot, FourWheelerSpot
from enums.spotType import SpotType
from enums.vehicleType import VehicleType


class ParkingSpotHelper():
    __spotServices = {
        SpotType.Small: SmallParkingService(),
        SpotType.Medium: MediumParkingService()
    }

    __vehicleSpotMap = {
        VehicleType.TwoWheeler: SpotType.Small,
        VehicleType.FourWheeler: SpotType.Medium,
    }

    def addSpot(self,spotNumber, spotType):
        if spotType in self.__spotServices:
            self.__spotServices[spotType].addSpot(spotNumber)
            self.__spotServices[spotType].printSpot()


    def getAvailableSpot(self,vehicle):
        key = vehicle.vehicleType
        if key in self.__vehicleSpotMap:
            # print(key)
            spotType = self.__vehicleSpotMap[key]
            # print(spotType)
            spotService = self.__spotServices[spotType]
            spot= spotService.getSpot()
            return spot
    
    def unPark(self, spot):
        spotService = self.__spotServices[spot.spotType]
        spotService.unPark(spot)



