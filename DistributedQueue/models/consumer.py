class Consumer:
    def __init__(self, name):
        self.__name = name
        self.__subscribeTopics = []
    
    def addTopic(self, topicName):
        self.__subscribeTopics.append(topicName)
        
    def removeTopic(self, topicName):
        self.__subscribeTopics.remove(topicName)
    
    
    
    