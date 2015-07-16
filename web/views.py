from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms.contact_form import ContactForm
from .forms.login_form import LoginForm, CreateLoginForm
import smtplib
from .models import *
from .servicecalls import salesreports, clientsreports
from .servicecalls.staffservice_gets import GetStaff
from .servicecalls.classservice_gets import GetClasses
from .servicecalls.appointmentservice_gets import GetScheduleItems
from .servicecalls.clientservice_inserts import AddNewClient
from .servicecalls.clientservice_gets import GetAllClients
from .servicecalls.siteservice_gets import GetSessionTypes
from .servicecalls.saleservice_gets import GetSales
from .session.login_manager import ConsumerCredentialManager
from html.parser import HTMLParser
from .decorators.auth_session import mbo_authed
from .decorators.thread_postpone import postpone
import datetime
from threading import Thread


def landing(request):
  context = { "page": "Welcome"}
  if 'userid' in request.session:
    context['userId'] = request.session['userid']
  return render(request, 'landing.html', context)


def contact(request):
  context = { "page": "Contact"}
  if 'userid' in request.session:
    context['userId'] = request.session['userid']
  if request.method == 'POST':
    form = ContactForm(data=request.POST)
    if form.is_valid():
      target_addresses = ['vacovsky@gmail.com']
      #below used to ensure both now and previous months have similar data to compare
      """
      try:
        if form.cleaned_data['cc_myself']:
          target_addresses.append(form.cleaned_data['contact_email'])

        send_mail(
        form.cleaned_data['message_subject'],
        form.cleaned_data['message_body'],
        form.cleaned_data['contact_email'],
        target_addresses
         )
      except:
        return render(request, 'contact.html',
          { 'page':'Contact',
            'form': form,
            'status':'There was a problem sending the message.  Please try again in a few minutes.'
                                                })
      """
      #form.save()
      message = 'This form is not live, but if you can easily change this in the source code of the project.'
      return render(request, 'contact.html', {'page':'Contact', 'form': form, 'message': message})
  else:
    form = ContactForm()
    return render(request, 'contact.html', {'page':'Contact', 'form': form})


def about(request):
  context = { "page": "About" }
  return render(request, 'about.html', context)


def sale_service(request):
  context = { "page": "Sales Report"}
  current_reports = salesreports.SalesReport()
  old_reports = salesreports.SalesReport(current=False)

  #turn this into a method - seems useful
  datacharts = ['total_dow', 'total_date', 'total_hour', 'total_paymenttype',
                'total_dow_nc', 'total_date_nc', 'total_hour_nc', 'total_paymenttype_nc' ]

  try:
    for i in datacharts:
      ReportsCacheModel.objects.filter(datapull_datestamp=datetime.datetime.today(), chart_name=i)[0]

  except:
    print('kicking off async soap call for sales report')
    context['spinner'] = True
    context['seconds'] = 90
    sales_report_helper()
    return render(request, 'please_wait.html', context)

  report = current_reports.sale_totals_by_date()
  piereport = current_reports.get_totals_by_payment_type()
  dowsales = current_reports.get_totals_by_dow()
  hoursales = current_reports.get_totals_by_hour()
  lm_report = old_reports.sale_totals_by_date()
  lm_piereport = old_reports.get_totals_by_payment_type()
  lm_dowsales = old_reports.get_totals_by_dow()
  lm_hoursales = old_reports.get_totals_by_hour()

  try:
    piereport, lm_piereport = salesreports.report_normalizer(piereport, lm_piereport)
  except:
    print("evaluation error in reports")

  context['salesreport'] = report
  context['piereport'] = piereport
  context['dowsalesreport'] = dowsales
  context['hoursalesreport'] = hoursales
  context['lm_salesreport'] = lm_report
  context['lm_piereport'] = lm_piereport
  context['lm_dowsalesreport'] = lm_dowsales
  context['lm_hoursalesreport'] = lm_hoursales
  return render(request, 'services/sales_report.html', context)


@postpone
def sales_report_helper():
  current_reports = salesreports.SalesReport()
  old_reports = salesreports.SalesReport(current=False)
  current_reports.sale_totals_by_date()
  current_reports.get_totals_by_payment_type()
  current_reports.get_totals_by_dow()
  current_reports.get_totals_by_hour()
  old_reports.sale_totals_by_date()
  old_reports.get_totals_by_payment_type()
  old_reports.get_totals_by_dow()
  old_reports.get_totals_by_hour()





def site_service(request):
  context = { "page": "Site Service"}
  context['services'] = GetSessionTypes().SessionTypes.SessionType
  return render(request, 'services/site.html', context)


def client_service(request):
  context = { "page": "My Profile"}
  if 'userid' in request.session:
    result = ConsumerCredentialManager(request.session['username'], request.session['password']).result
    context['clientprofile'] = result.Client
  return render(request, 'services/client.html', context)


def clients_report(request):
  context = { "page": "Clients Report"}
  datacharts = ['clients_by_age', 'clients_by_gender_pref', 'clients_by_sex']
  clientsreport = clientsreports.ClientsReport()

  #Experimentation with threading these calls
  try:
    for i in datacharts:
      ReportsCacheModel.objects.filter(datapull_datestamp=datetime.datetime.today(), chart_name=i)[0]
  except:
    print('kicking off async soap call for clients report')
    context['spinner'] = True
    context['seconds'] = 120
    clients_report_helper()
    return render(request, 'please_wait.html', context)

  context['clientage'] = clientsreport.all_clients_by_age()
  context['clientsex'] = clientsreport.client_sex()
  context['clientgp'] = clientsreport.client_gender_pref()
  context['first_appt_doy'] = clientsreport.first_appointment_doy()
  #context['first_appt_hour'] = clientsreport.first_appointment_hour
  context['first_appt_weekday'] = clientsreport.first_appointment_weekday()

  return render(request, 'services/clients_report.html', context)


@postpone
def clients_report_helper():
  clientsreport = clientsreports.ClientsReport()
  clientsreport.all_clients_by_age()
  clientsreport.client_sex()
  clientsreport.client_gender_pref()
  clientsreport.first_appointment_doy()
  clientsreport.first_appointment_weekday()



def appointment_service(request):
  context = { "page": "Appointment Service" }
  context['staffList'] = GetStaff().StaffMembers.Staff
  if request.method == 'POST':
    form = request.POST
    context['selectedStaff'] = form['staffid']
    schedItems = GetScheduleItems(staffId=form['staffid']).StaffMembers.Staff[0].Appointments
    if len(schedItems) > 0:
      context['scheduleItems'] = schedItems.Appointment
    else:
      context['message'] = "This staff member has no appointments today."
  return render(request, 'services/appointment.html', context)


def staff_service(request):
  if request.method == 'GET':
    context = { "page": "Staff Service"}
    context['staffList'] = GetStaff().StaffMembers.Staff
    return render(request, 'services/staff.html', context)


def class_service(request):
  if request.method == 'GET':
    context = { "page": "Class Service"}
    context['classList'] = GetClasses().Classes.Class
    return render(request, 'services/class.html', context)


@mbo_authed
def profile(request):
  if request.method == 'GET':
    context = { "page": "Profile"}
    return render(request, 'profile.html', context)


def log_in(request):
  request.session.flush()
  form = LoginForm()
  context = { "page": "Profile", 'form': form }
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    result = ConsumerCredentialManager(username, password).result

    try:
      userId = result.Client.ID
      request.session['userid'] = userId
      request.session['name'] = result.Client.FirstName + " " + result.Client.LastName
      request.session['username'] = username
      request.session['password'] = password

      if request.session['userid'] == None:
        context['errormsg'] = "The username or password you provided was invalid.  Please try again."

    except:
      context['errormsg'] = "The username or password you provided was invalid.  Please try again."
      request.session.flush()

  if 'userid' in request.session:
    return redirect('/web/services/client')
  return render(request, 'login.html', context)



def log_out(request):
  request.session.flush()
  return redirect('/web/login')


#@mbo_authed for protected pages

#TODO remove all the extra debugging stuff
def create_account(request):
  form = CreateLoginForm()
  context = { "page": "Create Account", 'form': form}
  if request.method == 'POST':
    try:
      username = request.POST['username']
      password = request.POST['password']
      password2 = request.POST['password']
      firstname = request.POST['firstName']
      lastname = request.POST['lastName']
      if password == password2:
        AddNewClient(username, password, firstname, lastname)

      result = ConsumerCredentialManager(username, password).result
      userId = result.Client.ID
      request.session['name'] = result.Client.FirstName + " " + result.Client.LastName
      request.session['userid'] = userId
      request.session['username'] = username
      request.session['password'] = password

      if request.session['userid'] == None:
        context['errormsg'] = "An issue was encountered while creating your account.  This message should handle errors better and based off the actual API Call results."
      else:
        redirect('/web/services/client')
    except:
      context["errormsg"]  = "An issue was encountered while creating your account.  This message should handle errors better and based off the actual API Call results."
      request.session.flush()
  return render(request, 'join.html', context)
