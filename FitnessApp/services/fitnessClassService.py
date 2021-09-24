from models.fitnessClass import FitnessClass

class FitnessClassService:
    def __init__(self):
        self.classes = {}

    def getClass(self, fitnessClassId):
        if fitnessClassId in self.classes:
            return self.classes[fitnessClassId]
        raise ValueError("error")

    def createClass(self, name, startTime, durationInMins, fitnessType, capacity):
        fitnessClass = FitnessClass(name, startTime, durationInMins, fitnessType, capacity)
        self.classes[fitnessClass.getId] = fitnessClass
        return fitnessClass.getId

    # def getAvailability(self, fitnessType):
    #     availClasses = filter(lambda x: x.fitnessType == fitnessType, self.classes)
    #     return availClasses


