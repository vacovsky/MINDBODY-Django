import operator
import datetime

class SalesReport:
  sale_totals_by_date = None
  sale_totals_by_payment_type = None
  sale_totals_by_dow = None

  def __init__(self, sales):
    #super(SalesReport, self).__init__(sales)
    self.SudsResult = sales
    self.SaleTotalsByDate = None
    #self.print_sales()

  def print_sales(self):
    for sale in self.SudsResult:
      print(sale)

  def sale_totals_by_date(self):
    sales = {}
    for sale in self.SudsResult:
      sale_total = 0.0
      payments = sale.Payments
      saledate = str(sale.SaleDate).split(' ')[0]

      for payment in payments:
        #print(payment[1])
        sale_total += payment[1][0].Amount

      if saledate not in sales:
        sales[saledate] = sale_total
      else:
        sales[saledate] += sale_total

    sale_totals_by_date = sales
    sorted_by_date = sorted(sale_totals_by_date.items(), key=operator.itemgetter(0))
    print(sorted_by_date)
    return sorted_by_date


  def get_totals_by_dow(self, comparison=0):
    sales = {}
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
    print(sorted_by_dow)
    return sorted_by_dow


  def get_totals_by_payment_type(self, comparison=0):
    sales = {}
    for sale in self.SudsResult:
      sale_total = 0.0
      payments = sale.Payments
      paytype = ""

      for payment in payments:
        #print(payment[1])
        paytype = payment[1][0].Type
        sale_total = payment[1][0].Amount
      if paytype not in sales:
        sales[paytype] = sale_total
      else:
        sales[paytype] += sale_total

    sale_totals_by_payment_type = sales
    sorted_by_payment_type = sorted(sale_totals_by_payment_type.items(), key=operator.itemgetter(0))
    print(sorted_by_payment_type)
    return sorted_by_payment_type