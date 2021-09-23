from helper import convert_time
from employee import Employee
from meeting import Meeting
from logic import Logic

class MeetingScheduler:
    employees = {}
    meetings = {}
    start_time = {}
    end_time = {}


    @staticmethod
    def add_employee(employee):
        if employee.id not in MeetingScheduler.employees:
            MeetingScheduler.employees[employee.get_name()] = employee
            return True
        print("employee already exist")
        return False

    @staticmethod
    def print_meeting():
        sort_dict = list(sorted(MeetingScheduler.meetings.items(), key = lambda x : x[1].start_time))
        for i in sort_dict:
            if i[1].is_scheduled:
                print(i[1].get_name() + ' ' + i[1].start_time_str + ' ' + i[1].end_time_str + ' ' + str(i[1].get_no_of_attendee()) + ' ' + str(i[1].get_organiser()))

    @staticmethod
    def is_conflict(meeting):
        for i in MeetingScheduler.start_time:
            # print(MeetingScheduler.start_time[i])
            # print(MeetingScheduler.end_time[i])
            if meeting.start_time >= MeetingScheduler.start_time[i] and meeting.start_time < MeetingScheduler.end_time[i]:
                return i
            elif meeting.end_time > MeetingScheduler.start_time[i] and meeting.end_time <= MeetingScheduler.end_time[i]:
                return i
        return None

    @staticmethod
    def resolve_conflict(conflict_meeting,meeting, employee):
        # import pdb
        # pdb.set_trace()
        for check in Logic:
            op = None
            if check.name == "CheckOrganiser":
                op = MeetingScheduler.compare_organiser(conflict_meeting,meeting, employee)
            elif check.name == "CheckDesignation":
                op = MeetingScheduler.compare_designation(conflict_meeting,meeting)
            elif check.name == "CheckAttendee":
                op = MeetingScheduler.compare_no_of_attendee(conflict_meeting,meeting)
            elif check.name == "CheckForMaxmium":
                op = MeetingScheduler.compare_meeting_end_time(conflict_meeting,meeting)
            else:
                print("No logic matches")

            if op:
                if op.id == meeting.id:
                    del (MeetingScheduler.start_time[conflict_meeting.id])
                    del (MeetingScheduler.end_time[conflict_meeting.id])
                    MeetingScheduler.meetings[conflict_meeting.id].is_scheduled = False
                return op
        return op

    @staticmethod
    def add_meeting(meeting, organiser_name, employee_name):
        if meeting.id in MeetingScheduler.meetings:
            print("meeting already exist")
            return False
        if organiser_name not in MeetingScheduler.employees:
            print("organiser doesn't exist")
            return False
        if employee_name not in MeetingScheduler.employees:
            print("employee doesn't exist")
            return False
        organiser = MeetingScheduler.employees[organiser_name]
        employee = MeetingScheduler.employees[employee_name]
        meeting.add_organiser(organiser_name)
        organiser.add_meeting(meeting.id)
        # import pdb
        # pdb.set_trace()
        while(True):
            conflict_meeting_id = MeetingScheduler.is_conflict(meeting)
            if conflict_meeting_id:
                conflict_meeting = MeetingScheduler.meetings[conflict_meeting_id]
                result = MeetingScheduler.resolve_conflict(conflict_meeting, meeting, employee)
                if not result:
                    print("got some error")
                    return False
                if result.id == conflict_meeting.id:
                    return True
                else:
                    continue
            else:
                MeetingScheduler.meetings[meeting.id] = meeting
                MeetingScheduler.start_time[meeting.id] = meeting.start_time
                MeetingScheduler.end_time[meeting.id] = meeting.end_time
                return True

    @staticmethod
    def compare_organiser(conflict_meeting, new_meeting, employee):
        if employee.get_name() == conflict_meeting.get_organiser() and employee.get_name() == new_meeting.get_organiser():
            return False
        elif employee.get_name() == conflict_meeting.get_organiser():
            return conflict_meeting
        elif employee.get_name() == new_meeting.get_organiser():
            return new_meeting
        else:
            return None

    @staticmethod
    def compare_designation(conflict_meeting, new_meeting):
        print(conflict_meeting.__dict__)
        print(new_meeting.__dict__)
        conflict_meeting_organiser = MeetingScheduler.employees[conflict_meeting.get_organiser()]
        new_meeting_organiser = MeetingScheduler.employees[new_meeting.get_organiser()]

        if conflict_meeting_organiser.get_designation().value < new_meeting_organiser.get_designation().value:
            return conflict_meeting
        elif conflict_meeting_organiser.get_designation().value > new_meeting_organiser.get_designation().value:
            return new_meeting
        else:
            return None

    @staticmethod
    def compare_no_of_attendee(conflict_meeting, new_meeting):

        if conflict_meeting.get_no_of_attendee() < new_meeting.get_no_of_attendee():
            return new_meeting
        elif conflict_meeting.get_no_of_attendee() > new_meeting.get_no_of_attendee():
            return new_meeting
        else:
            return None

    @staticmethod
    def compare_meeting_end_time(conflict_meeting, new_meeting):

        if conflict_meeting.end_time <= new_meeting.end_time:
            return conflict_meeting
        else:
            return new_meeting




