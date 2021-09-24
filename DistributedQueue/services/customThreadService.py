from models.customThread import CustomThread
from singleton_decorator import singleton

@singleton
class CustomThreadService:
    def __init__(self):
        self.__threads = {}

    def startListening(self, consumerName, func, *args):
        thread = CustomThread(consumerName, func, args)
        thread.start()
        self.__threads[consumerName + args[0]] = thread
    
    def stopListening(self, consumerName, topicName):
        print("stopListening", consumerName, topicName)
        key = consumerName + topicName
        if key in self.__threads:
            print("stopListening", consumerName, topicName, key)
            thread = self.__threads[key]
            thread.kill()
            thread.join()
            print("killed")