import sys
sys.path.insert(0, '../Models')

from user import User
from datetime import datetime

class UserService:
    users = []

    @staticmethod
    def add_user(name, phone):
        u = User(name, phone)
        UserService.users.append(u)
        return u

    # @staticmethod
    # def start_user_session(user_id, booking_id):
    #     UserService.user_sessions[user_id] = {
    #         "datetime":datetime.now(),
    #         "booking_id": booking_id,
    #         "is_active": True 
    #     }
    #     
    # 
    # @staticmethod
    # def mark_session_as_inactive(user_id, booking_id):
    #     if user_id in UserService.user_session:
    #         del UserService.user_session[user_id]
    # 
    # @staticmethod
    # def verify_session(self):
    #     timeout = datetime.timedelta(minutes= 1)
    #     for user_id in UserService.user_session:
    #         if UserService.user_session[user_id] + timeout < datetime.now():
    #             del UserService.user_session[user_id]




