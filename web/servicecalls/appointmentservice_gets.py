
from helpers.mbosoap.AppointmentService import AppointmentServiceCalls

def GetScheduleItems(staffId=None):
    staff = []
    if staffId != None:
        staff.append(staffId)
    result = AppointmentServiceCalls().GetScheduleItems(staffIds=staff)
    return result
