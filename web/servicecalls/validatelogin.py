
from helpers.mbosoap.ClientService import ClientServiceCalls
from suds.sudsobject import asdict, Printer, items, footprint


def ValidateLogin(username, password):
  validated = ClientServiceCalls().ValidateLogin(username=username, password=password)
  return validated
