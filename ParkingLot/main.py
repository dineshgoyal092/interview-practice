from services.parkingService import ParkingService
from services.ticketService import TicketService
from services.rateService import RateService
from services.parkingSpotHelper import ParkingSpotHelper
# from controller.parkingController import ParkingController
from enums.vehicleType import VehicleType
from enums.spotType import SpotType
from models.vehicle import TwoWheeler, FourWheeler


#add rate card hourly
rateService = RateService()
rateService.addRateSlabHourly(VehicleType.TwoWheeler, 2, 20)
rateService.addRateSlabHourly(VehicleType.TwoWheeler, 2, 50)
rateService.addRateSlabHourly(VehicleType.TwoWheeler, 20, 80)

#add rate card daily
rateService.updateDailyRate(VehicleType.TwoWheeler, 80)

#add rate card hourly
rateService.addRateSlabHourly(VehicleType.FourWheeler, 1, 30)
rateService.addRateSlabHourly(VehicleType.FourWheeler, 2, 50)
rateService.addRateSlabHourly(VehicleType.FourWheeler, 21, 100)

#add rate card daily
rateService.updateDailyRate(VehicleType.FourWheeler, 100)


parkingSpotHelper = ParkingSpotHelper()

#add differnt spot into parking area
print("adding small spots")
spotNumber = 1
parkingSpotHelper.addSpot(spotNumber, SpotType.Small)
spotNumber += 1
parkingSpotHelper.addSpot(spotNumber, SpotType.Small)

print("adding medium spots")
spotNumber += 1
parkingSpotHelper.addSpot(spotNumber, SpotType.Medium)
spotNumber += 1
parkingSpotHelper.addSpot(spotNumber, SpotType.Medium)


ticketService = TicketService()
parkingService = ParkingService(rateService, parkingSpotHelper, ticketService)

# create vehicle object
twoWheeler1 = TwoWheeler("MH01WE1234")
twoWheeler2 = TwoWheeler("MH01WE1235")
twoWheeler3 = TwoWheeler("MH01WE1236")
fourWheeler1 = FourWheeler("KA01WE1236")
fourWheeler2 = FourWheeler("KA01WE1237")
fourWheeler3 = FourWheeler("KA01WE1238")



print("start Parking")
print(parkingService.park(twoWheeler1))
print(parkingService.park(twoWheeler2))
print(parkingService.park(fourWheeler1))
print(parkingService.park(fourWheeler2))
print(parkingService.park(fourWheeler3))
print(parkingService.park(twoWheeler3))


print("start unParking")
print("price", parkingService.unPark(twoWheeler1))
print("price", parkingService.unPark(twoWheeler2))
print("price", parkingService.unPark(fourWheeler1))
print("price", parkingService.unPark(fourWheeler2))

print("park again")
print(parkingService.park(twoWheeler1))
print(parkingService.park(twoWheeler2))
print(parkingService.park(fourWheeler1))
print(parkingService.park(fourWheeler2))

print("start unParking")
print("price", parkingService.unPark(twoWheeler1))
print("price", parkingService.unPark(twoWheeler2))
print("price", parkingService.unPark(fourWheeler1))
print("price", parkingService.unPark(fourWheeler2))

print("vehicle parking history")
print(ticketService.getVehicleLogs("MH01WE1234"))
print(ticketService.getVehicleLogs("MH01WE1235"))
print(ticketService.getVehicleLogs("KA01WE1236"))
print(ticketService.getVehicleLogs("KA01WE1237"))







