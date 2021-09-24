# import sys
# sys.path.insert(0,"../models")
from models.user import User

class UserService:
    userMap = {}
    
    @staticmethod
    def addUser(name):
        user = User(name)
        UserService.userMap[user.id] = user
        return user

    @staticmethod
    def getUser(id):
        return UserService.userMap.get(id)
    
    
        
        