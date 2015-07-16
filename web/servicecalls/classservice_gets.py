
from helpers.mbosoap.ClassService import ClassServiceCalls

def GetClasses():
    classlist = ClassServiceCalls().GetClasses()
    return classlist
