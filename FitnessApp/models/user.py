import uuid
from enums.role import Role
class User:
    def __init__(self, name, email=None, role=Role.Normal):
        self.__id = uuid.uuid1()
        self.__name = name
        self.__email = email
        self.__role = role
