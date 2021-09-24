from services.fitnessClassService import FitnessClassService

class FitnessClassController:
    def __init__(self):
        self.fitnessClassService = FitnessClassService()

    def addClass(self, name, startTime, durationInMins, fitnessType, capacity):
        return self.fitnessClassService.createClass(name, startTime, durationInMins, fitnessType, capacity)

