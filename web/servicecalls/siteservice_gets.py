
from helpers.mbosoap.SiteService import SiteServiceCalls

def GetSessionTypes():
    sessiontypes = SiteServiceCalls().GetSessionTypes()
    return sessiontypes
