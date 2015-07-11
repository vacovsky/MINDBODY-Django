
from helpers.mbosoap.AppointmentService import AppointmentServiceCalls
from suds.sudsobject import asdict, Printer, items, footprint

def GetScheduleItems(staffId=None):
  staff = []
  if staffId != None:
   staff.append(staffId)
  result = AppointmentServiceCalls().GetScheduleItems(staffIds=staff)
  return result