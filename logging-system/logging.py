from datetime import datetime
import threading
import time
class Loging:
    __instance = None
    __method  = ["console","database","file","kafka"]
    __db_ptr  = 0
    __kafka_ptr = 0

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Loging.__instance == None:
            Loging()
        return Loging.__instance

    def __init__(self):
        if Loging.__instance != None:
            pass
        else:
            Loging.__instance = self
            self.__log_file = open("log.txt", 'a+')
            print(self.__method)
            if "database" in self.__method:
                Loging.db_thread = threading.Thread(target=self.update_db, args=())
                Loging.db_thread.start()
            if "kafka" in self.__method:
                Loging.kafka_thread = threading.Thread(target=self.update_kafka, args=())
                Loging.kafka_thread.start()


    def error(self, msg):
        log_msg = " Error: " + msg
        self.print_to_log(log_msg)

    def info(self, msg):
        log_msg = " Info: " + msg
        self.print_to_log(log_msg)

    def debug(self, msg):
        log_msg = " Debug: " + msg
        self.print_to_log(log_msg)

    def print_to_log(self, msg):
        if "console" in self.__method:
            print(str(datetime.now()) + msg,)

        if "database" in self.__method or "kafka" in self.__method or "file" in self.__method:
            line = str(datetime.now()) + msg + "\n"
            self.__log_file.write(line)

        # if "database" in self.__method:
        #
        #     pass
        #     # write_to_databse(self.log_file)
        #
        # if "kafka" in self.__method:
        #     pass
        #     # write_to_kafka(self.log_file)
        #
        # if "file" in self.__method:
        #     pass
        #     # write_to_kafka(self.log_file)

    @staticmethod
    def update_db():
        while(True):
            with open("log.txt","r") as f:
                str = f.readline(Loging.__db_ptr)
                if str:
                    print("writing to db line number  " + str(Loging.__db_ptr))
                    Loging.__db_ptr += 1
                    time.sleep(2)



    @staticmethod
    def update_kafka():
        while (True):
            with open("log.txt","r") as f:
                str = f.readline(Loging.__kafka_ptr)
                if str:
                    print("writing to kafka line number  " + str(Loging.__kafka_ptr))
                    Loging.__kafka_ptr += 1
                    time.sleep(2)




