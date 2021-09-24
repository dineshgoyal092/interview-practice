from models.topic import Topic
from singleton_decorator import singleton

@singleton
class TopicService:
    def __init__(self):
        self.__topics = {}
    
    def getTopic(self, topicName):
        self.__topics.get(topicName)
    
    def addTopic(self, topicName):
        topic = Topic(topicName)
        self.__topics[topicName] = topic
        return topic

    def getNextMessage(self, topicName):
        if topicName in self.__topics:
            topic = self.__topics[topicName]
            return topic.getNextMessage()

    def addMessage(self, topicName, message):
        if topicName in self.__topics:
            topic = self.__topics[topicName]
            topic.addMessage(message)