"""These lines may be helpful in debugging code you are running.
   Just import this before running your call to return SOAP requests
   and responses to the console."""


"""
import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
"""

from suds.plugin import MessagePlugin

class LogPlugin(MessagePlugin):
  def sending(self, context):
    print(str(context.envelope))
  def received(self, context):
    print(str(context.reply))
