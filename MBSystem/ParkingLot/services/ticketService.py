from models.ticket import Ticket
from datetime import datetime

class TicketService:
    def __init__(self):
        self.__tickets = []

    def createTicket(self, spot, vehicle):
        ticket = Ticket(datetime.now(), vehicle.vehicleNumber, spot, vehicle.vehicleType)
        self.__tickets.append(ticket)
        return ticket

    def getVehicleLogs(self, vehicleNumber):
        vehicleLogs = filter(lambda x: x.getVehicleNumber() == vehicleNumber, self.__tickets)
        result = []
        for log in vehicleLogs:
            result.append({"vehicleNumber": log.getVehicleNumber(), "durationInHrs": log.durationInHrs, "amountPaid":log.getAmount()})

        return result

    def recordPayment(self, ticket, price):
        ticket.setAmount(price)
        ticket.setDuration()
        
