import uuid

class User:
    def __init__(self, name):
        if not name: raise Exception("name cannot be empty")
        self.__id = uuid.uuid4()
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        print("hello")
        if not name: raise Exception("name cannot be empty")
        self.__name = name
        
# u1 = User("Dinesh")
# print(u1.__dict__)
# u2 = User("Dinesh1")
# print(u2.__dict__)
# u2 = User("Dinesh2")
# print(u2.__dict__)
#         
        

