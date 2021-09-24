class TopicController:
    def __init__(self, topicService):
        self.__topicService = topicService

    def addTopic(self, topicName):
        self.__topicService.addTopic(topicName)

    def getTopic(self, topicName):
        return self.__topicService.getTopic(topicName)

    # def getNextMessage(self, topicName):
    #     return self.__topicService.getNextMessage(topicName)

    def addMessage(self, topicName, message):
        return self.__topicService.addMessage(topicName, message)