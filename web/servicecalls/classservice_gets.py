
from helpers.mbosoap.ClassService import ClassServiceCalls
from suds.sudsobject import asdict, Printer, items, footprint

def GetClasses(startDate=None):
   classlist = ClassServiceCalls().GetClasses()
   return classlist
