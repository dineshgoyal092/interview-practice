from models.producer import Producer
from singleton_decorator import singleton

@singleton
class ProducerService:
    def __init__(self):
        self.__producers = {}

    def getProducer(self, producerName):
        return self.__producers.get(producerName)

    def addProducer(self, producerName):
        producer = Producer(producerName)
        self.__producers[producerName] = producer
        return producer