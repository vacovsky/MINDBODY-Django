import dateutil.relativedelta
from helpers.mbosoap.SaleService import SaleServiceCalls, SaleServiceMethods
from suds.sudsobject import asdict, Printer, items, footprint
from helpers.mbosoap.BasicRequestHelper import *
from datetime import datetime


def GetSales(timedelta=1, timeunit='months'):
  end = datetime.today()
  start = end - dateutil.relativedelta.relativedelta(months=timedelta)
  result = SaleServiceCalls().GetSales(startSaleDateTime=start.date(), endSaleDateTime=end.date())
  return result
