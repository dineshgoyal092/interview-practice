import uuid

def validateSplit(byPercentage, splitInfo, amount):
    if byPercentage and splitInfo:
        totalPercentage = 100.0
        for splitEntry in splitInfo:
            totalPercentage -= splitEntry.get("percentage", 0)
        if totalPercentage != 0.0:
            raise ValueError("Percentage split doesn't match")
    elif splitInfo:
        totalAmount = amount
        for splitEntry in splitInfo:
            totalAmount -= splitEntry.get("amount", 0)
        if totalAmount != 0.0:
            raise ValueError("Total amount split doesn't match")
        
        
class Bill:
    
    def __init__(self, amount, paidBy, createdBy, byPercentage = False, splitInfo = None):
        
        if not amount or amount < 0.0 or not paidBy or not createdBy:
            raise ValueError('Input is not valid')
        
        validateSplit(amount, byPercentage, splitInfo)
                
        self.__id = uuid.uuid4()
        self.__amount = amount
        self.__paidBy = paidBy
        self.__createdBy = createdBy
        if not splitInfo:
            self.__splitInfo[paidBy] = (100.0, amount)
        else:
            for splitEntry in splitInfo:
                self.__splitInfo[splitEntry["userId"]] = (splitEntry.get("percentage"), splitEntry.get("amount"))
    
    def getId(self):
        return self.__id
    
            
    
    def addSplit(self, splitInfo, byPercentage):
        validateSplit(self.amount, byPercentage, splitInfo)
        if splitInfo:
            self.__splitInfo = {}
            for splitEntry in splitInfo:
                self.__splitInfo[splitEntry["userId"]] = (splitEntry.get("percentage"), splitEntry.get("amount"))
        