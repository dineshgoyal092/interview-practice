# import sys
# sys.path.insert(0,"../models")
from models.bill import Bill
from models.user import User
from singleton_decorator import singleton

@singleton
class BillService:
    
    def __init__(self):
        self.__billMap = {}
        self.__userBillMap = {}

    def addBill(self,amount, paidBy, createdBy, byPercentage = False, splitInfo = None):
        bill = Bill(amount, paidBy, createdBy, byPercentage, splitInfo)
        BillService.__billMap[bill.id] = bill
        if not splitInfo:
            if "paidBy" in self.__userBillMap:
                self.__userBillMap[paidBy].append(bill.id)
            else:
                self.__userBillMap[paidBy] = [bill.id]
        else:
            for splitEntry in splitInfo:
                if "userId" in splitEntry and splitEntry["userId"] in self.__userBillMap:
                    self.__userBillMap[splitEntry["userId"]].append(bill.id)
                else:
                    self.__userBillMap[splitEntry["userId"]] = [bill.id]
        return bill


    def getBill(self,id):
        return self.__billMap.get(id)
    
    def getUserBills(self, userId):
        listOfUserBills = []
        if userId in self.__userBillMap:
            for billId in self.__userBillMap[userId]:
                listOfUserBills.append(self.__billMap.get(id))
        return  listOfUserBills            