
from helpers.mbosoap.SiteService import SiteServiceCalls, SiteServiceMethods
from suds.sudsobject import asdict, Printer, items, footprint


def GetSessionTypes():
  sessiontypes = SiteServiceCalls().GetSessionTypes()
  return sessiontypes

