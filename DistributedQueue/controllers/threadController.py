# class ThreadController:
#     def __init__(self, threadService, messageService):
#         self.__threadService = threadService
#         self.__messageService = messageService
# 
#     def addListner(self, consumerName, topicName):
#         self.__threadService.addThread(consumerName, topicName, self.__messageService)
# 
#     def removeListner(self, consumerName, topicName):
#         return self.__threadService.killThread(consumerName, topicName)