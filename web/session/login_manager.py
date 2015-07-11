
from ..servicecalls.validatelogin import ValidateLogin


class ConsumerCredentialManager:
  userId = None
  result = None
  def __init__(self, username, password):
    self.logged_in = False
    self.username = username
    self.password = password
    self.userId = None
    self.result = None
    self.check_login()



  def check_login(self):
    try:
      validate_result = ValidateLogin(self.username, self.password)
      self.userId = validate_result.Client.ID
      userId = self.userId
      self.result = validate_result

    except:
      userId = None
      self.userId = None


