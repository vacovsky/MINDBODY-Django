
from helpers.mbosoap.ClientService import ClientServiceCalls


def ValidateLogin(username, password):
    validated = ClientServiceCalls().ValidateLogin(username=username, password=password)
    return validated
