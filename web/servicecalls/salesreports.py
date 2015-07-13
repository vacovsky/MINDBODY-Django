import operator
import datetime
from ..models import ReportsCacheModel
import ast
from ..servicecalls.saleservice_gets import GetSales

class SalesReport:
  sale_totals_by_date = None
  sale_totals_by_payment_type = None
  sale_totals_by_dow = None
  sale_totals_by_hour = None

  def __init__(self, sales=None, current=True):
    self.SudsResult = sales
    self.SaleTotalsByDate = None
    self.current = current
    self.TodayDate = datetime.datetime.today()

  def GetSudsResults(self):
    if not self.current:
      self.SudsResult = GetSales(timedelta=1).Sales.Sale
    else:
      self.SudsResult = GetSales(timedelta=2).Sales.Sale

  def print_sales(self):
    for sale in self.SudsResult:
      print(sale)

  def get_totals_by_dow(self, comparison=0):
    name = 'total_dow'
    if not self.current:
      name += '_nc'
    sales = {}
    try:
      sorted_by_dow = ReportsCacheModel.objects.get(datapull_datestamp=self.TodayDate, chart_name=name)
      return eval(sorted_by_dow.data_string)

    except ReportsCacheModel.DoesNotExist:
      if self.SudsResult == None:
        self.GetSudsResults()

      for sale in self.SudsResult:
        sale_total = 0.0
        payments = sale.Payments
        saleday = str(sale.SaleDate.weekday())
        for payment in payments:
          sale_total += payment[1][0].Amount
        if saleday not in sales:
          sales[saleday] = sale_total
        else:
          sales[saleday] += sale_total
      sale_totals_by_dow = sales
      sorted_by_dow = sorted(sale_totals_by_dow.items(), key=operator.itemgetter(0))

      report = ReportsCacheModel()
      report.chart_name = name
      report.data_string = str(sorted_by_dow)
      report.save()

      return sorted_by_dow

  def sale_totals_by_date(self):
    name = 'total_date'
    if not self.current:
      name += '_nc'
    sales = {}

    try:
      sorted_by_payment_type = ReportsCacheModel.objects.get(datapull_datestamp=self.TodayDate, chart_name=name)
      return eval(sorted_by_payment_type.data_string)

    except ReportsCacheModel.DoesNotExist:
      if self.SudsResult == None:
        self.GetSudsResults()

      for sale in self.SudsResult:
        sale_total = 0.0
        payments = sale.Payments
        saledate = str(sale.SaleDate).split(' ')[0]
        for payment in payments:
          sale_total += payment[1][0].Amount
        if saledate not in sales:
          sales[saledate] = sale_total
        else:
          sales[saledate] += sale_total
      sale_totals_by_date = sales
      sorted_by_date = sorted(sale_totals_by_date.items(), key=operator.itemgetter(0))

      report = ReportsCacheModel()
      report.chart_name = name
      report.data_string = str(sorted_by_date)
      report.save()

      return sorted_by_date

  def get_totals_by_hour(self, comparison=0):
    name = 'total_hour'
    if not self.current:
      name += '_nc'
    sales = {}

    try:
      sale_by_hour = ReportsCacheModel.objects.get(datapull_datestamp=self.TodayDate, chart_name=name)
      return eval(sale_by_hour.data_string)

    except ReportsCacheModel.DoesNotExist:
      if self.SudsResult == None:
        self.GetSudsResults()

      for sale in self.SudsResult:
        sale_total = 0.0
        payments = sale.Payments
        salehour = str(sale.SaleDateTime.hour)
        if len(salehour) == 1:
          salehour = '0' + str(salehour)
        else:
          salehour = str(salehour)
        for payment in payments:
          sale_total += payment[1][0].Amount
        if salehour not in sales:
          sales[salehour] = sale_total
        else:
          sales[salehour] += sale_total
      sale_totals_by_hour = sales
      sale_by_hour = sorted(sale_totals_by_hour.items(), key=operator.itemgetter(0))

      report = ReportsCacheModel()
      report.chart_name = name
      report.data_string = str(sale_by_hour)
      report.save()

      return sale_by_hour

  def get_totals_by_payment_type(self, comparison=0):
    name = 'total_paymenttype'
    if not self.current:
      name += '_nc'
    sales = {}
    sale_list = ''

    try:
      sorted_by_payment_type = ReportsCacheModel.objects.get(datapull_datestamp=self.TodayDate, chart_name=name)
      return ast.literal_eval(sorted_by_payment_type.data_string)

    except ReportsCacheModel.DoesNotExist:
      if self.SudsResult == None:
        self.GetSudsResults()

      for sale in self.SudsResult:
        sale_total = 0.0
        payments = sale.Payments
        paytype = ""
        for payment in payments:
          paytype = str(payment[1][0].Type)
          sale_total = payment[1][0].Amount
        if paytype not in sales:
          sales[paytype] = sale_total
        else:
          sales[paytype] += sale_total
      sale_totals_by_payment_type = sales
      sorted_by_payment_type = sorted(sale_totals_by_payment_type.items(), key=operator.itemgetter(1))

      report = ReportsCacheModel()
      report.chart_name = name
      report.data_string = '\"' + str(sale_totals_by_payment_type) + '\"'
      report.save()

      return sale_totals_by_payment_type.items


def report_normalizer(report1, report2):
  print(report1)
  print(eval(report1))
  print(type(eval(report1)))

  """
  for i in report1:
    exists = False
    for k in report2:
      if i[0] == k[0]:
        exists = True
    if not exists:
      report2.insert(report1.index(i), (i[0], 0))

  for i in report2:
    exists = False
    for k in report1:
      if i[0] == k[0]:
        exists = True
    if not exists:
      report1.insert(report2.index(i), (i[0], 0))
  """
  return eval(report1).items, eval(report2).items
