class UserController:
    def __init__(self, userService):
        self.userService = userService

    def addUser(self, name):
        return self.userService.addUser(name)