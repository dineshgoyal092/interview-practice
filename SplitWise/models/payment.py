import uuid
class Payment:
    def __init__(self, amount, paidBy, paidTo):
        self.__id = uuid.uuid4()
        self.__amount = amount
        self.__padiBy = paidBy
        self.__paidTo = paidTo