from datetime import datetime
import math

class RateService:
    def __init__(self):
        self.__rateSlabsHourly = {}
        self.__rateDaily = {}
        
    def addRateSlabHourly(self, vehicleType, noOfHr, rate):
        if vehicleType in self.__rateSlabsHourly:
            self.__rateSlabsHourly[vehicleType].append((noOfHr, rate))
        else:
            self.__rateSlabsHourly[vehicleType] = [(noOfHr, rate)]
    
    def updateDailyRate(self, vehicleType, rate):
        if vehicleType in self.__rateDaily:
            self.__rateDaily[vehicleType] = rate
        else:
            self.__rateDaily[vehicleType] = rate
            
    def getPrice(self, ticket):
        import time
        time.sleep(1)
        now = datetime.now()
        startTime = ticket.startTime 
        delta = now - startTime
        parkedHrs = int(math.ceil(delta.seconds / 3600))
        print("parkedHours-", parkedHrs, ticket.getVehicleNumber())
        totalPrice = 0
        
        if parkedHrs > 24:
            totalPrice = delta.days * self.__rateDaily[ticket.vehicleType]
            return totalPrice
        
        for rate in self.__rateSlabsHourly[ticket.getVehicleType()]:
            if parkedHrs > rate[0]:
                totalPrice = rate[1]
                parkedHrs -= rate[0]
            else:
                totalPrice = rate[1]
                break
        return totalPrice
            