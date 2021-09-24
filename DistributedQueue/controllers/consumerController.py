from topicController import TopicController

class ConsumerController:
    def __init__(self, consumerService, listnerService, messageService):
        self.__consumerService = consumerService
        self.__listnerService = listnerService
        self.__messageService = messageService

    def addConsumer(self, consumerName):
        self.__consumerService.addConsumer(consumerName)

    def getConsumer(self, consumerName):
        return self.__consumerService.getConsumer(consumerName)

    def subscribeToTopic(self, consumerName, topicName):
        self.__consumerService.addTopic(consumerName, topicName)
        self.__listnerService.startListening(consumerName, self.__messageService.getNextMessage, topicName)
    
    def unSubscribeToTopic(self, consumerName, topicName):
        self.__consumerService.removeTopic(consumerName, topicName)
        self.__listnerService.stopListening(consumerName, topicName)