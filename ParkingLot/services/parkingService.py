from models.ticket import Ticket
from datetime import datetime

class ParkingService:
    def __init__(self, rateService, parkingSpotHelper, ticketService):
        self.__rateService = rateService
        self.__parkingSpotHelper = parkingSpotHelper
        self.__ticketService = ticketService

    def park(self, vehicle):
        spot = self.__parkingSpotHelper.getAvailableSpot(vehicle)
        if spot:
            spot.parkVehicle(vehicle)
            # print(spot.__dict__)
            ticket = self.__ticketService.createTicket(spot, vehicle)
            vehicle.assignTicket(ticket)
            return f"Vehicle Number- {vehicle.vehicleNumber} SpotNumber- {spot.spotNumber}"
        else:
            return f"{vehicle.vehicleNumber} no spot available"
        
    def unPark(self, vehicle):
        ticket  = vehicle.ticket
        self.__parkingSpotHelper.unPark(ticket.getSpot())
        price = self.__rateService.getPrice(ticket)
        self.__ticketService.recordPayment(ticket, price)
        ticket.setAmount(price)
        return price
        
        
        

    
    

            

    