class Topic:
    def __init__(self, name):
        self.__name = name
        self.__queue = []
        self.__offset = 0
        self.__length = 0
    
    def getNextMessage(self):
        if self.__offset < self.__length:
            message = self.__queue[self.__offset]
            self.__offset += 1
            return message
    
    def addMessage(self, message):
        self.__queue.append(message)
        self.__length += 1
        
        