from helpers.mbosoap.ClientService import ClientServiceCalls, ClientServiceMethods
from suds.sudsobject import asdict, Printer, items, footprint
from helpers.mbosoap.BasicRequestHelper import *
from datetime import datetime


def GetAllClients(page=0):
  results = ClientServiceMethods().GetAllClients(page=page)
  #print(results)
  return results