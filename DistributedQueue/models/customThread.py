import threading
import time
import uuid

class CustomThread(threading.Thread):
    
    # overriding constructor
    def __init__(self, consumerName, func, args, sleep_interval=3):
        # calling parent class constructor
        threading.Thread.__init__(self)
        self.__id = uuid.uuid4()
        self.__consumerName = consumerName
        # self.__topicName = topicName
        self.__kill = False
        self.__func = func
        self.__args = args
        self.__interval = sleep_interval

    # define your own run method
    def run(self):
        while True:
            if self.__kill:
                break
            # print("listening", self.__consumerName)
            time.sleep(self.__interval)
            message = self.__func(self.__args[0])
            if message:
                print(self.__consumerName, "received", message.text)


    def kill(self):
        self.__kill = True
