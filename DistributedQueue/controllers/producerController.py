class ProducerController:
    def __init__(self, producerService):
        self.__producerService = producerService

    def addProducer(self, producerName):
        self.__producerService.addProducer(producerName)

    def getProducer(self, producerName):
        return self.__producerService.getProducer(producerName)
    
    