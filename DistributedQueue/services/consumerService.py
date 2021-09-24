from models.consumer import Consumer
from singleton_decorator import singleton

@singleton
class ConsumerService:
    def __init__(self):
        self.__consumers = {}

    def getConsumer(self, consumerName):
        return self.__consumers.get(consumerName)

    def addConsumer(self, consumerName):
        consumer = Consumer(consumerName)
        self.__consumers[consumerName] = consumer
        return consumer
    
    def addTopic(self, consumerName, topicName):
        if consumerName in self.__consumers:
            consumer = self.__consumers[consumerName]
            consumer.addTopic(topicName)

    def removeTopic(self, consumerName, topicName):
        if consumerName in self.__consumers:
            consumer = self.__consumers[consumerName]
            consumer.removeTopic(topicName)
        