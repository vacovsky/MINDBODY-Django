from datetime import datetime
from suds.client import Client
try:
    from . import BasicRequestHelper
except:
    import BasicRequestHelper


from suds.plugin import MessagePlugin


class LogPlugin(MessagePlugin):

    def sending(self, context):
        print(str(context.envelope))

    def received(self, context):
        print(str(context.reply))

#client = Client("http://localhost/wsdl.wsdl", plugins=[LogPlugin()])


class AppointmentServiceCalls():

    """This class contains examples of consumer methods for each AppointmentService method."""

    """AddOrUpdateAppointments Methods"""

    def AddOrUpdateAppointments(self, updateAction="AddNew",
                                test=False,
                                sendEmail=False,
                                applyPayment=True,
                                appointments=None):
        result = AppointmentServiceMethods().AddOrUpdateAppointments(updateAction,
                                                                     test,
                                                                     sendEmail,
                                                                     applyPayment,
                                                                     appointments)
        return result

    """AddOrUpdateAvailabilities Methods"""

    def AddOrUpdateAvailabilities(self, updateAction="AddNew",
                                  test=False,
                                  availabilityIds=None,
                                  locationId=None,
                                  staffIds=None,
                                  programIds=None,
                                  startDateTime=datetime.today(),
                                  endDateTime=datetime.today(),
                                  daysOfWeek=None,
                                  unavailableDescription=None,
                                  isUnavailable=False,
                                  publicDisplay=None):
        result = AppointmentServiceMethods().AddOrUpdateAvailabilities(updateAction,
                                                                       test,
                                                                       availabilityIds,
                                                                       locationId,
                                                                       staffIds,
                                                                       programIds,
                                                                       startDateTime,
                                                                       endDateTime,
                                                                       daysOfWeek,
                                                                       unavailableDescription,
                                                                       isUnavailable,
                                                                       publicDisplay)
        return result

    """GetActiveSessionTimes Methods"""

    def GetActiveSessionTimes(self, scheduleType=None,
                              sessionTypeIds=None,
                              startTime=datetime.today(),
                              endTime=datetime.today()):
        result = AppointmentServiceMethods().GetActiveSessionTimes(scheduleType,
                                                                   sessionTypeIds,
                                                                   startTime,
                                                                   endTime)
        return result

    """GetAppointmentOptions Methods"""

    def GetAppointmentOptions(self):
        result = AppointmentServiceMethods().GetAppointmentOptions()
        return result

    """GetBookableItems Methods"""

    def GetBookableItems(self, sessionTypeIds,
                         locationIds=None,
                         staffIds=None,
                         startDate=datetime.today(),
                         endDate=datetime.today()):
        result = AppointmentServiceMethods().GetBookableItems(sessionTypeIds,
                                                              locationIds,
                                                              staffIds,
                                                              startDate,
                                                              endDate)
        return result

    """GetScheduleItems Methods"""

    def GetScheduleItems(self, locationIds=None,
                         staffIds=None,
                         startDate=datetime.today(),
                         endDate=datetime.today(),
                         ignorePrepFinishTimes=False):
        result = AppointmentServiceMethods().GetScheduleItems(locationIds,
                                                              staffIds,
                                                              startDate,
                                                              endDate,
                                                              ignorePrepFinishTimes)
        return result

    """GetStaffAppointments Methods"""

    def GetStaffAppointments(self, staffUsername=None,
                             staffPassword=None,
                             siteIds=None,
                             appointmentIds=None,
                             locationIds=None,
                             startDate=datetime.today(),
                             endDate=datetime.today(),
                             staffIds=None,
                             clientIds=None):
        result = AppointmentServiceMethods().GetStaffAppointments(staffUsername,
                                                                  staffPassword,
                                                                  siteIds,
                                                                  appointmentIds,
                                                                  locationIds,
                                                                  startDate,
                                                                  endDate,
                                                                  staffIds,
                                                                  clientIds)
        return result


class AppointmentServiceMethods():

    """This class contains producer methods for all AppointmentService methods."""
    wsdl = BasicRequestHelper.BuildWsdlUrl("Appointment")
    service = Client(wsdl)
    # uncomment below line for debug
    #service = Client(wsdl, plugins=[LogPlugin()])

    def CreateBasicRequest(self, requestName):
        return BasicRequestHelper.CreateBasicRequest(self.service, requestName)

    """AddOrUpdateAppointments methods"""
    def AddOrUpdateAppointments(self,
                                updateAction,
                                test,
                                sendEmail,
                                applyPayment,
                                appointments):
        request = self.CreateBasicRequest("AddOrUpdateAppointments")

        request.UpdateAction = updateAction
        request.Test = test
        request.SendEmail = sendEmail
        request.ApplyPayment = applyPayment
        request.Appointments = BasicRequestHelper.FillArrayType(
            self.service, appointments, "Appointment", "Appointment")

        return self.service.service.AddOrUpdateAppointments(request)

    """AddOrUpdateAvailabilities methods"""

    def AddOrUpdateAvailabilities(self, updateAction,
                                  test,
                                  availabilityIds,
                                  locationId,
                                  staffIds,
                                  programIds,
                                  startDateTime,
                                  endDateTime,
                                  daysOfWeek,
                                  unavailableDescription,
                                  isUnavailable,
                                  publicDisplay):
        request = self.CreateBasicRequest("AddOrUpdateAvailabilities")

        request.UpdateAction = updateAction
        request.Test = test
        request.AvailabilityIDs = BasicRequestHelper.FillArrayType(
            self.service, availabilityIds, "Int")
        request.StaffIDs = BasicRequestHelper.FillArrayType(self.service, staffIds, "Long")
        request.ProgramIDs = BasicRequestHelper.FillArrayType(self.service, programIds, "Int")
        request.StartDateTime = startDateTime
        request.EndDateTime = endDateTime
        request.DaysOfWeek = BasicRequestHelper.FillArrayType(
            self.service, daysOfWeek, "DayOfWeek", "DayOfWeek")
        # Only used when IsUnavailable is true.
        request.UnavailableDescription = unavailableDescription
        request.LocationID = locationId  # Only used when IsUnavailable is false.
        request.IsUnavailable = isUnavailable
        request.PublicDisplay = BasicRequestHelper.SetEnumerable(
            self.service, "AvailabilityDisplay", publicDisplay)

        return self.service.service.AddOrUpdateAvailabilities(request)

    """GetActiveSessionTimes methods"""

    def GetActiveSessionTimes(self, scheduleType,
                              sessionTypeIds,
                              startTime,
                              endTime):
        request = self.CreateBasicRequest("GetActiveSessionTimes")

        request.ScheduleType = BasicRequestHelper.SetEnumerable(
            self.service, "ScheduleType", scheduleType)
        request.SessionTypeIDs = BasicRequestHelper.FillArrayType(
            self.service, sessionTypeIds, "Int")
        request.StartTime = startTime
        request.EndTime = endTime

        return self.service.service.GetActiveSessionTimes(request)

    """GetAppointmentOptions methods"""

    def GetAppointmentOptions(self):
        request = self.CreateBasicRequest("GetAppointmentOptions")

        return self.service.service.GetAppointmentOptions(request)

    """GetBookableItems methods"""

    def GetBookableItems(self, sessionTypeIds, locationIds, staffIds, startDate, endDate):
        request = self.CreateBasicRequest("GetBookableItems")

        request.SessionTypeIDs = BasicRequestHelper.FillArrayType(
            self.service, sessionTypeIds, "Int")
        request.LocationIDs = BasicRequestHelper.FillArrayType(self.service, locationIds, "Int")
        request.StaffIDs = BasicRequestHelper.FillArrayType(self.service, staffIds, "Long")
        request.StartDate = startDate
        request.EndDate = endDate

        return self.service.service.GetBookableItems(request)

    """GetScheduleItems methods"""

    def GetScheduleItems(self, locationIds, staffIds, startDate, endDate, ignorePrepFinishTimes):
        request = self.CreateBasicRequest("GetScheduleItems")

        request.LocationIDs = BasicRequestHelper.FillArrayType(self.service, locationIds, "Int")
        request.StaffIDs = BasicRequestHelper.FillArrayType(self.service, staffIds, "Long")
        request.StartDate = startDate
        request.EndDate = endDate
        request.IgnorePrepFinishTimes = ignorePrepFinishTimes

        return self.service.service.GetScheduleItems(request)

    """GetStaffAppointments methods"""

    def GetStaffAppointments(self, staffUsername,
                             staffPassword,
                             siteIds,
                             appointmentIds,
                             locationIds,
                             startDate,
                             endDate,
                             staffIds,
                             clientIds):
        request = self.CreateBasicRequest("GetStaffAppointments")

        request.StaffCredentials = BasicRequestHelper.CreateStaffCredentials(
            self.service, staffUsername, staffPassword, siteIds)
        request.AppointmentIDs = BasicRequestHelper.FillArrayType(
            self.service, appointmentIds, "Int")
        request.LocationIDs = BasicRequestHelper.FillArrayType(self.service, locationIds, "Int")
        request.StartDate = startDate
        request.EndDate = endDate
        request.StaffIDs = BasicRequestHelper.FillArrayType(self.service, staffIds, "Long")
        request.ClientIDs = BasicRequestHelper.FillArrayType(self.service, clientIds, "String")

        return self.service.service.GetStaffAppointments(request)
