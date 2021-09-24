class Message:
    def __init__(self, text, producer):
        self.__text = text
        self.__producer = producer
        
    @property
    def text(self):
        return self.__text