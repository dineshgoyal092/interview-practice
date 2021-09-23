from helper import get_time
class Meeting:
    id = 0
    def __init__(self, name, start_time, end_time, no_of_attendee):
        Meeting.id += 1
        self.id = Meeting.id
        self.__name = name
        self.start_time_str = start_time
        self.end_time_str = end_time
        self.__no_of_attendee = no_of_attendee
        self.__organiser_name = None
        self.is_scheduled = True

    @property
    def start_time(self):
        return get_time(self.start_time_str)

    @property
    def end_time(self):
        return get_time(self.end_time_str)


    def get_name(self):
        return self.__name

    def get_organiser(self):
        return self.__organiser_name

    def get_no_of_attendee(self):
        return self.__no_of_attendee

    def add_organiser(self, employee_name):
        self.__organiser_name = employee_name.lower()



