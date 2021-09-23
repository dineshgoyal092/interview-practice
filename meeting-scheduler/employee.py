class Employee:
    id = 0
    def __init__(self, name, designation):
        Employee.id += 1
        self.id = Employee.id
        self.__name = name.lower()
        self.__designation = designation
        self.meeting_scheduled = []


    def get_name(self):
        return self.__name.lower()

    def get_designation(self):
        print(self.__designation.name)
        print(self.__designation.value)
        return self.__designation

    def add_meeting(self, meeting_id):
        if meeting_id not in self.meeting_scheduled:
            self.meeting_scheduled.append(meeting_id)
            return True
        else:
            print("already added in employee")
            return False





