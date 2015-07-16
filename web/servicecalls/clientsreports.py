import operator
import datetime
from ..models import ReportsCacheModel
import ast
from .clientservice_gets import GetAllClients
from dateutil.relativedelta import relativedelta

from ..decorators.thread_postpone import postpone


class ClientsReport:
  clients_by_age_group = None
  all_clients_by_sex = None
  all_clients_by_gp = None


  def __init__(self, clients=None, current=True):
    self.SudsResult = clients
    self.current = current
    self.TodayDate = datetime.datetime.today()


  def GetSudsResults(self):
    index = 1
    tpc = 0
    result = GetAllClients()
    self.SudsResult = [result.Clients.Client]
    tpc = result.TotalPageCount

    while index < tpc:
      print(index, tpc)
      index += 1
      self.SudsResult.append(GetAllClients(page=index).Clients.Client)


  def print_clients(self):
    for sale in self.SudsResult:
      print(sale)


  def all_clients_by_age(self):
    name = 'clients_by_age'
    if not self.current:
      name += '_nc'
    ages = {}
    try:
      clients_by_age = ReportsCacheModel.objects.filter(datapull_datestamp=self.TodayDate, chart_name=name)[0]
      return eval(clients_by_age.data_string)

    except (IndexError, ReportsCacheModel.DoesNotExist):
      if self.SudsResult == None:
        self.GetSudsResults()

      for thing in self.SudsResult:
        for client in thing:
          age = 0
          if client.BirthDate != None:
            birthday = client.BirthDate
            age = relativedelta(self.TodayDate, birthday).years

            if age != 0:
              if age <= 20:
                if "-20" in ages:
                  ages['-20'] += 1
                else:
                  ages['-20'] = 1

              if age > 20 and age <= 25:
                if "21-25" in ages:
                  ages['21-25'] += 1
                else:
                  ages['21-25'] = 1

              if age > 25 and age <= 30:
                if "26-30" in ages:
                  ages['26-30'] += 1
                else:
                  ages['26-30'] = 1

              if age > 30 and age <= 35:
                if "31-35" in ages:
                  ages['31-35'] += 1
                else:
                  ages['31-35'] = 1

              if age > 35 and age <= 40:
                if "36-40" in ages:
                  ages['36-40'] += 1
                else:
                  ages['36-40'] = 1

              if age > 40 and age <= 45:
                if "41-45" in ages:
                  ages['41-45'] += 1
                else:
                  ages['41-45'] = 1

              if age > 45 and age <= 50:
                if "46-50" in ages:
                  ages['46-50'] += 1
                else:
                  ages['46-50'] = 1

              if age > 50 and age <= 55:
                if "51-55" in ages:
                  ages['51-55'] += 1
                else:
                  ages['51-55'] = 1

              if age > 55 and age <= 60:
                if "56-60" in ages:
                  ages['56-60'] += 1
                else:
                  ages['56-60'] = 1

              if age > 60 and age <= 65:
                if "61-65" in ages:
                  ages['61-65'] += 1
                else:
                  ages['61-65'] = 1

              if age > 65:
                if "65+" in ages:
                  ages['65+'] += 1
                else:
                  ages['65+'] = 1

      clients_by_age_group = ages
      ages_by_group = sorted(clients_by_age_group.items(), key=operator.itemgetter(0))

      report = ReportsCacheModel()
      report.chart_name = name
      report.data_string = str(ages_by_group)
      report.save()

      return ages_by_group


  def client_sex(self):
      name = 'clients_by_sex'
      if not self.current:
        name += '_nc'
      sexes = {}
      try:
        all_clients_by_sex = ReportsCacheModel.objects.filter(datapull_datestamp=self.TodayDate, chart_name=name)[0]
        return eval(all_clients_by_sex.data_string)

      except (IndexError, ReportsCacheModel.DoesNotExist):
        if self.SudsResult == None:
          self.GetSudsResults()

        for thing in self.SudsResult:
          for client in thing:
            if hasattr(client, 'Gender') and client.Gender != None:
              gender = client.Gender

              if gender == 'Male':
                if "Male" in sexes:
                  sexes['Male'] += 1
                else:
                  sexes['Male'] = 1

              elif gender == 'Female':
                if "Female" in sexes:
                  sexes['Female'] += 1
                else:
                  sexes['Female'] = 1

              else:
                if "Other" in sexes:
                  sexes['Other'] += 1
                else:
                  sexes['Other'] = 1


        clients_by_sex = sexes
        all_clients_by_sex = sorted(clients_by_sex.items(), key=operator.itemgetter(0))

        report = ReportsCacheModel()
        report.chart_name = name
        report.data_string = str(all_clients_by_sex)
        report.save()

        return all_clients_by_sex


  def client_gender_pref(self):
      name = 'clients_by_gender_pref'
      if not self.current:
        name += '_nc'
      sexes = {}
      try:
        all_clients_by_gp = ReportsCacheModel.objects.filter(datapull_datestamp=self.TodayDate, chart_name=name)[0]
        return eval(all_clients_by_gp.data_string)

      except (IndexError, ReportsCacheModel.DoesNotExist):
        if self.SudsResult == None:
          self.GetSudsResults()
        for thing in self.SudsResult:
          for client in thing:
            if client.AppointmentGenderPreference != None:
              gender = client.AppointmentGenderPreference

              if gender == 'Male':
                if "Male" in sexes:
                  sexes['Male'] += 1
                else:
                  sexes['Male'] = 1

              elif gender == 'Female':
                if "Female" in sexes:
                  sexes['Female'] += 1
                else:
                  sexes['Female'] = 1

              else:
                if "None" in sexes:
                  sexes['None'] += 1
                else:
                  sexes['None'] = 1


        clients_by_gp = sexes
        all_clients_by_gp = sorted(clients_by_gp.items(), key=operator.itemgetter(0))

        report = ReportsCacheModel()
        report.chart_name = name
        report.data_string = str(all_clients_by_gp)
        report.save()

        return all_clients_by_gp


  def first_appointment_doy(self):
      name = 'first_appt_doy'
      if not self.current:
        name += '_nc'
      date_hits = {}
      try:
        first_appt_doy = ReportsCacheModel.objects.filter(datapull_datestamp=self.TodayDate, chart_name=name)[0]
        return eval(first_appt_doy.data_string)

      except (IndexError, ReportsCacheModel.DoesNotExist):
        if self.SudsResult == None:
          self.GetSudsResults()

        for thing in self.SudsResult:
          for client in thing:
            firstappt = None
            if client.FirstAppointmentDate != None:
              #firstappt = str('%02d' % client.FirstAppointmentDate.month) + '-' + str(client.FirstAppointmentDate.day)

              #firstappt = next_weekday(client.FirstAppointmentDate, 0)
              firstappt = 'Week ' + str('%02d' % client.FirstAppointmentDate.isocalendar()[1])

              if firstappt not in date_hits:
                date_hits[firstappt] = 1
              else:
                date_hits[firstappt] += 1

        first_appointment_doy = date_hits
        first_appt_doy = sorted(first_appointment_doy.items(), key=operator.itemgetter(0))

        report = ReportsCacheModel()
        report.chart_name = name
        report.data_string = str(first_appt_doy)
        report.save()

        return first_appt_doy

  """


  def first_appointment_hour(self):
        name = 'first_appt_hour'
        if not self.current:
          name += '_nc'
        date_hits = {}
        try:
          first_appt_hour = ReportsCacheModel.objects.filter(datapull_datestamp=self.TodayDate, chart_name=name)[0]
          return eval(first_appt_hour.data_string)

        except (IndexError, ReportsCacheModel.DoesNotExist):
          if self.SudsResult == None:
            self.GetSudsResults()

          for thing in self.SudsResult:
            for client in thing:
              firstappt = None
              if client.FirstAppointmentDate != None:
                #firstappt = str('%02d' % client.FirstAppointmentDate.month) + '-' + str(client.FirstAppointmentDate.day)

                #firstappt = next_weekday(client.FirstAppointmentDate, 0)
                firstappt = str(client.FirstAppointmentDate.hour)
                if len(firstappt) == 1:
                  firstappt = '0' + str(firstappt)

                if firstappt not in date_hits:
                  date_hits[firstappt] = 1
                else:
                  date_hits[firstappt] += 1

          first_appointment_hour = date_hits
          first_appt_hour = sorted(first_appointment_hour.items(), key=operator.itemgetter(0))

          report = ReportsCacheModel()
          report.chart_name = name
          report.data_string = str(first_appt_hour)
          report.save()

          return first_appt_hour
  """


  def first_appointment_weekday(self):
        name = 'first_appt_weekday'
        if not self.current:
          name += '_nc'
        date_hits = {}
        try:
          first_appt_weekday = ReportsCacheModel.objects.filter(datapull_datestamp=self.TodayDate, chart_name=name)[0]
          return eval(first_appt_weekday.data_string)

        except (IndexError, ReportsCacheModel.DoesNotExist):
          if self.SudsResult == None:
            self.GetSudsResults()

          for thing in self.SudsResult:
            for client in thing:
              firstappt = None
              if client.FirstAppointmentDate != None:
                #firstappt = str('%02d' % client.FirstAppointmentDate.month) + '-' + str(client.FirstAppointmentDate.day)
                #firstappt = next_weekday(client.FirstAppointmentDate, 0)
                firstappt = client.FirstAppointmentDate.weekday()

                if firstappt not in date_hits:
                  date_hits[firstappt] = 1
                else:
                  date_hits[firstappt] += 1

          first_appointment_weekday = date_hits
          first_appt_weekday = sorted(first_appointment_weekday.items(), key=operator.itemgetter(0))

          report = ReportsCacheModel()
          report.chart_name = name
          report.data_string = str(first_appt_weekday)
          report.save()

          return first_appt_weekday


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)
