from designation_rank import DesignationRank
from employee import Employee
from meeting import Meeting
from db_helper import MeetingScheduler
from helper import get_time

def main():
    with open("employee.txt",'r') as f:
        for i in f:
            print(i)
            input = i.split(',')
            if len(input) != 2:
                print("employee input not correct ")
                return False
            employee_name = input[0]
            designation = input[1].replace('\n','')
            if designation in  DesignationRank.__members__:
                employee = Employee(employee_name, DesignationRank[designation])
                if not MeetingScheduler.add_employee(employee):
                    print("error while adding user")
            else:
                print("designation doesn't match")

    for i in MeetingScheduler.employees:
        print(i)
    with open("meeting.txt",'r') as f:
        employee_name = f.readline().replace('\n','')
        for i in f:
            # print(i)
            input = i.split(',')
            if len(input) != 5:
                print("meeting input not correct ")
                # print(input)
                return False
            meeting_name = input[0]
            start_time = input[1]
            end_time = input[2]
            no_of_attendee = int(input[3])
            organiser_name = input[4].replace('\n','')
            meeting = Meeting(meeting_name,start_time,end_time,no_of_attendee)
            if not MeetingScheduler.add_meeting(meeting, organiser_name.lower(), employee_name.lower()):
                print("error while adding meeting")
            print("\n")
    MeetingScheduler.print_meeting()

main()
