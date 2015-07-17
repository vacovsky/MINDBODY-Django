from helpers.mbosoap.ClientService import ClientServiceMethods
from helpers.mbosoap.BasicRequestHelper import *


def GetAllClients(page=0):
    results = ClientServiceMethods().GetAllClients(page=page)
    #print(results)
    return results
