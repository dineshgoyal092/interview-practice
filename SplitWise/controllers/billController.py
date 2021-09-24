# import sys
# sys.path.insert(0,"../services")
# sys.path.insert(0,"../models")
#
# from billService import BillService
class BillController:
    def __init__(self, billService):
        self.billService = billService

    def addBill(self, amount, paidBy, createdBy, byPercentage = False, splitInfo = None):
        self.billService.addBill(amount, paidBy, createdBy, byPercentage, splitInfo)
        
    