from helpers.mbosoap.ClientService import ClientServiceMethods
from helpers.mbosoap.BasicRequestHelper import FillArrayType
from datetime import datetime

def AddNewClient(username, password, firstname="Not", lastname="Provided", birthdate=datetime.today()):
    service = ClientServiceMethods()
    client = service.service.factory.create("Client")
    client.Username = username
    client.Password = password
    client.FirstName = firstname
    client.LastName = lastname
    client.BirthDate = birthdate
    client.Action = None
    clients = FillArrayType(service.service, [client], "Client", "Client")
    result = ClientServiceMethods().AddOrUpdateClients('AddNew', False, clients)
    return result
