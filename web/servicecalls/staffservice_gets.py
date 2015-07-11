
from helpers.mbosoap.StaffService import StaffServiceCalls
from suds.sudsobject import asdict, Printer, items, footprint


def GetStaff():
  stafflist = StaffServiceCalls().GetStaff(staffIds=None,
                           staffUsername=None,
                           staffPassword=None,
                           siteIds=None,
                           filters=None,
                           sessionTypeId=None,
                           startDateTime=None,
                           locationId=None)
  return stafflist

