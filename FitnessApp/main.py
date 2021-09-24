from controllers.bookingController import BookingController
from controllers.fitnessClassController import FitnessClassController
from services.fitnessClassService import FitnessClassService
from services.waitListService import WaitListService
from enums.fitnessType import FitnessType

fitnessClassService = FitnessClassService()
waitListService = WaitListService()
bookingController = BookingController(fitnessClassService, waitListService)
fitnessClassController = FitnessClassController()


from datetime import datetime

with open("sample.txt",'r') as f:
    f.readline()
    for i in f:
        print(i)
        input = i.split()
        name = str(input[0])
        startTime = datetime.strptime(str(input[1]), '%Y-%m-%d-%H-%M-%S')
        durationInMins = int(input[2])
        fitnessType = FitnessType(input[3])
        print(fitnessType)
        capacity = int(input[4])
        finessClass = fitnessClassController.addClass(name, startTime, durationInMins, fitnessType, capacity)
        print(finessClass.__dict__)

with open("sample.txt",'r') as f:
    f.readline()
    for i in f:
        print(i)
        input = i.split()
        name = str(input[0])
        startTime = datetime.strptime(str(input[1]), '%Y-%m-%d-%H-%M-%S')
        durationInMins = int(input[2])
        fitnessType = FitnessType(input[3])
        print(fitnessType)
        capacity = int(input[4])
        finessClass = fitnessClassController.addClass(name, startTime, durationInMins, fitnessType, capacity)
        print(finessClass.__dict__)
