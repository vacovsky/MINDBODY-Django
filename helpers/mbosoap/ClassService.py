from suds.client import Client
try:
    from . import BasicRequestHelper
except:
    import BasicRequestHelper
from datetime import datetime


class ClassServiceCalls:

    """This class contains examples of consumer methods for each ClientService method."""

    """AddClientsToClasses Methods"""

    def AddClientsToClasses(self, clientIds,
                            classIds,
                            test=False,
                            requirePayment=False,
                            waitList=False,
                            sendEmail=False):
        result = ClassServiceMethods().AddClientsToClasses(clientIds,
                                                           classIds,
                                                           test,
                                                           requirePayment,
                                                           waitList,
                                                           sendEmail)
        return result

    """AddClientsToEnrollments Methods"""

    def AddClientsToEnrollments(self, clientIds,
                                classScheduleIds=None,
                                courseIds=None,
                                enrollDateForward=datetime.today(),
                                enrollOpen=datetime.today(),
                                test=False,
                                sendEmail=False,
                                waitlist=False):
        """Note that either ClassScheduleIDs or CourseIDs can be passed in. If both are passed, the API call ignores CourseIDs."""
        result = ClassServiceMethods().AddClientsToEnrollments(clientIds,
                                                               classScheduleIds,
                                                               courseIds,
                                                               enrollDateForward,
                                                               enrollOpen,
                                                               test,
                                                               sendEmail,
                                                               waitlist)
        return result

    """GetClassDescriptions Methods"""

    def GetClassDescriptions(self, classDescId=None,
                             programId=None,
                             staffIds=None,
                             locationId=None,
                             startClassDateTime=datetime.today(),
                             endClassDateTime=datetime.today()):
        result = ClassServiceMethods().GetClassDescriptions(classDescId,
                                                            programId,
                                                            staffIds,
                                                            locationId,
                                                            startClassDateTime,
                                                            endClassDateTime)
        return result

    """GetClasses Methods"""

    def GetClasses(self, classDescIds=None,
                   classIds=None,
                   staffIds=None,
                   startDateTime=datetime.today(),
                   endDateTime=datetime.today(),
                   clientId=None,
                   programIds=None,
                   sessionTypeIds=None,
                   locationIds=None,
                   semesterIds=None,
                   hideCanceledClasses=False,
                   schedulingWindow=False):
        result = ClassServiceMethods().GetClasses(classDescIds,
                                                  classIds,
                                                  staffIds,
                                                  startDateTime,
                                                  endDateTime,
                                                  clientId,
                                                  programIds,
                                                  sessionTypeIds,
                                                  locationIds,
                                                  semesterIds,
                                                  hideCanceledClasses,
                                                  schedulingWindow)
        return result

    def GetClassesSince(self, sinceDate):
        self.GetClasses(startDateTime=sinceDate)

    def GetClassesForClient(self, clientId):
        self.GetClasses(clientId=clientId)

    """GetClassSchedules Methods"""

    def GetClassSchedules(self, locationIds=None,
                          classScheduleIds=None,
                          staffIds=None,
                          programIds=None,
                          sessionTypeIds=None,
                          startDate=datetime.today(),
                          endDate=datetime.today()):
        result = ClassServiceMethods().GetClassSchedules(locationIds,
                                                         classScheduleIds,
                                                         staffIds,
                                                         programIds,
                                                         sessionTypeIds,
                                                         startDate,
                                                         endDate)
        return result

    """GetClassVisits Methods"""

    def GetClassVisits(self, classId):
        result = ClassServiceMethods().GetClassVisits(classId)
        return result

    """GetCourses Methods"""

    def GetCourses(self, locationIds=None,
                   courseIds=None,
                   staffIds=None,
                   programIds=None,
                   startDate=datetime.today(),
                   endDate=datetime.today(),
                   semesterIds=None):
        result = ClassServiceMethods().GetCourses(locationIds,
                                                  courseIds,
                                                  staffIds,
                                                  programIds,
                                                  startDate,
                                                  endDate,
                                                  semesterIds)
        return result

    """GetEnrollments Methods"""

    def GetEnrollments(self, locationIds=None,
                       classScheduleIds=None,
                       staffIds=None,
                       programIds=None,
                       sessionTypeIds=None,
                       semesterIds=None,
                       courseIds=None,
                       startDate=datetime.today(),
                       endDate=datetime.today()):
        result = ClassServiceMethods().GetEnrollments(locationIds,
                                                      classScheduleIds,
                                                      staffIds,
                                                      programIds,
                                                      sessionTypeIds,
                                                      semesterIds,
                                                      courseIds,
                                                      startDate,
                                                      endDate)
        return result

    """GetSemesters Methods"""

    def GetSemesters(self, semesterIds=None,
                     startDate=datetime.today(),
                     endDate=datetime.today()):
        result = ClassServiceMethods().GetSemesters(semesterIds,
                                                    startDate,
                                                    endDate)
        return result

    """GetWaitlistEntries Methods"""

    def GetWaitlistEntries(self, classScheduleIds=None,
                           clientIds=None,
                           waitlistEntryIds=None,
                           classIds=None):
        result = ClassServiceMethods().GetWaitlistEntries(classScheduleIds,
                                                          clientIds,
                                                          waitlistEntryIds,
                                                          classIds)
        return result

    """RemoveClientsFromClasses Methods"""

    def RemoveClientsFromClasses(self, clientIds,
                                 classIds,
                                 test=False,
                                 sendEmail=False,
                                 lateCancel=False):
        result = ClassServiceMethods().RemoveClientsFromClasses(clientIds,
                                                                classIds,
                                                                test,
                                                                sendEmail,
                                                                lateCancel)
        return result

    """RemoveFromWaitlist Methods"""

    def RemoveFromWaitlist(self, waitlistEntryIds):
        result = ClassServiceMethods().RemoveFromWaitlist(waitlistEntryIds)
        return result

    """UpdateClientVisits Methods"""

    def UpdateClientVisits(self, visits=None,
                           test=False,
                           sendEmail=False):
        result = ClassServiceMethods().UpdateClientVisits(visits,
                                                          test,
                                                          sendEmail)
        return result

    def ToggleMakeUpOnAllVisitsForAClass(self, classId,
                                         test=False,
                                         sendEmail=False):
        """This method will toggle the MakeUp field of every visit for a class."""
        visits = ClassServiceMethods().GetClassVisits(classId).Class.Visits.Visit
        for Visit in visits:
            Visit.MakeUp = not Visit.MakeUp
        self.UpdateClientVisits(visits, test, sendEmail)


class ClassServiceMethods:

    """This class contains producer methods for all ClassService methods."""
    wsdl = BasicRequestHelper.BuildWsdlUrl("Class")
    service = Client(wsdl)

    def CreateBasicRequest(self, requestName):
        return BasicRequestHelper.CreateBasicRequest(self.service, requestName)

    """AddClientsToClasses methods"""

    def AddClientsToClasses(self, clientIds,
                            classIds,
                            test,
                            requirePayment,
                            waitlist,
                            sendEmail):
        request = self.CreateBasicRequest("AddClientsToClasses")

        request.ClientIDs = BasicRequestHelper.FillArrayType(self.service, clientIds, "String")
        request.ClassIDs = BasicRequestHelper.FillArrayType(self.service, classIds, "Int")
        request.Test = test
        request.RequirePayment = requirePayment
        request.Waitlist = waitlist
        request.SendEmail = sendEmail

        return self.service.service.AddClientsToClasses(request)

    """AddClientsToEnrollments methods"""

    def AddClientsToEnrollments(self, clientIds,
                                classScheduleIds,
                                courseIds,
                                enrollDateForward,
                                enrollOpen,
                                test,
                                sendEmail,
                                waitlist):
        """Note that if classScheduleIds and courseIds are both passed in, only classScheduleIds are used."""
        request = self.CreateBasicRequest("AddClientsToEnrollments")

        request.ClientIDs = BasicRequestHelper.FillArrayType(self.service, clientIds, "String")
        request.ClassScheduleIDs = BasicRequestHelper.FillArrayType(
            self.service, classScheduleIds, "Int")
        request.CourseIDs = BasicRequestHelper.FillArrayType(self.service, courseIds, "Long")
        request.EnrollDateForward = enrollDateForward
        request.EnrollOpen = BasicRequestHelper.FillArrayType(
            self.service, enrollOpen, "DateTime", "dateTime")
        request.Test = test
        request.SendEmail = sendEmail
        request.Waitlist = waitlist

        return self.service.service.AddClientsToEnrollments(request)

    """GetClassDescriptions Methods"""

    def GetClassDescriptions(self, classDescId,
                             programIds,
                             staffIds,
                             locationIds,
                             startClassDateTime,
                             endClassDateTime):
        """Note that although this call accepts arrays for all ID fields, it only uses the first value in each array."""
        request = self.CreateBasicRequest("GetClassDescriptions")

        request.ClassDescriptionIDs = BasicRequestHelper.FillArrayType(
            self.service, classDescId, "Int")
        request.ProgramIDs = BasicRequestHelper.FillArrayType(self.service, programIds, "Int")
        request.StaffIDs = BasicRequestHelper.FillArrayType(self.service, staffIds, "Long")
        request.LocationIDs = BasicRequestHelper.FillArrayType(self.service, locationIds, "Int")
        request.StartClassDateTime = startClassDateTime
        request.EndClassDateTime = endClassDateTime

        return self.service.service.GetClassDescriptions(request)

    """GetClasses methods"""

    def GetClasses(self, classDescIds,
                   classIds,
                   staffIds,
                   startDateTime,
                   endDateTime,
                   clientId,
                   programIds,
                   sessionTypeIds,
                   locationIds,
                   semesterIds,
                   hideCanceledClasses,
                   schedulingWindow):
        request = self.CreateBasicRequest("GetClasses")

        request.ClassDescriptionIDs = BasicRequestHelper.FillArrayType(
            self.service, classDescIds, "Int")
        request.ClassIDs = BasicRequestHelper.FillArrayType(self.service, classIds, "Int")
        request.StaffIDs = BasicRequestHelper.FillArrayType(self.service, staffIds, "Long")
        request.StartDateTime = startDateTime
        request.EndDateTime = endDateTime
        request.ClientID = clientId
        request.ProgramIDs = BasicRequestHelper.FillArrayType(self.service, programIds, "Int")
        request.SessionTypeIDs = BasicRequestHelper.FillArrayType(
            self.service, sessionTypeIds, "Int")
        request.LocationIDs = BasicRequestHelper.FillArrayType(self.service, locationIds, "Int")
        request.SemesterIDs = BasicRequestHelper.FillArrayType(self.service, semesterIds, "Int")
        request.HideCanceledClasses = hideCanceledClasses
        request.SchedulingWindow = schedulingWindow

        return self.service.service.GetClasses(request)

    """GetClassSchedules methods"""

    def GetClassSchedules(self, locationIds,
                          classScheduleIds,
                          staffIds,
                          programIds,
                          sessionTypeIds,
                          startDate,
                          endDate):
        request = self.CreateBasicRequest("GetClassSchedules")

        request.LocationIDs = BasicRequestHelper.FillArrayType(self.service, locationIds, "Int")
        request.ClassScheduleIDs = BasicRequestHelper.FillArrayType(
            self.service, classScheduleIds, "Int")
        request.StaffIDs = BasicRequestHelper.FillArrayType(self.service, staffIds, "Long")
        request.ProgramIDs = BasicRequestHelper.FillArrayType(self.service, programIds, "Int")
        request.SessionTypeIDs = BasicRequestHelper.FillArrayType(
            self.service, sessionTypeIds, "Int")
        request.StartDate = startDate
        request.EndDate = endDate

        return self.service.service.GetClassSchedules(request)

    """GetClassVisits methods"""

    def GetClassVisits(self, classId):
        request = self.CreateBasicRequest("GetClassVisits")

        request.ClassID = classId

        return self.service.service.GetClassVisits(request)

    """GetCourses methods"""

    def GetCourses(self, locationIds,
                   courseIds,
                   staffIds,
                   programIds,
                   startDate,
                   endDate,
                   semesterIds):
        request = self.CreateBasicRequest("GetCourses")

        request.LocationIDs = BasicRequestHelper.FillArrayType(self.service, locationIds, "Int")
        request.CourseIDs = BasicRequestHelper.FillArrayType(self.service, courseIds, "Long")
        request.StaffIDs = BasicRequestHelper.FillArrayType(self.service, staffIds, "Long")
        request.ProgramIDs = BasicRequestHelper.FillArrayType(self.service, programIds, "Int")
        request.StartDate = startDate
        request.EndDate = endDate
        request.SemesterIDs = BasicRequestHelper.FillArrayType(self.service, semesterIds, "Int")

        return self.service.service.GetCourses(request)

    """GetEnrollments methods"""

    def GetEnrollments(self, locationIds,
                       classScheduleIds,
                       staffIds,
                       programIds,
                       sessionTypeIds,
                       semesterIds,
                       courseIds,
                       startDate,
                       endDate):
        request = self.CreateBasicRequest("GetEnrollments")

        request.LocationIDs = BasicRequestHelper.FillArrayType(self.service, locationIds, "Int")
        request.ClassScheduleIDs = BasicRequestHelper.FillArrayType(
            self.service, classScheduleIds, "Int")
        request.StaffIDs = BasicRequestHelper.FillArrayType(self.service, staffIds, "Long")
        request.ProgramIDs = BasicRequestHelper.FillArrayType(self.service, programIds, "Int")
        request.SessionTypeIDs = BasicRequestHelper.FillArrayType(
            self.service, sessionTypeIds, "Int")
        request.SemesterIDs = BasicRequestHelper.FillArrayType(self.service, semesterIds, "Int")
        request.CourseIDs = BasicRequestHelper.FillArrayType(self.service, courseIds, "Long")
        request.StartDate = startDate
        request.EndDate = endDate

        return self.service.service.GetEnrollments(request)

    """GetSemesters methods"""

    def GetSemesters(self, semesterIds,
                     startDate,
                     endDate):
        request = self.CreateBasicRequest("GetSemesters")

        request.SemesterIDs = BasicRequestHelper.FillArrayType(self.service, semesterIds, "Int")
        request.StartDate = startDate
        request.EndDate = endDate

        return self.service.service.GetSemesters(request)

    """GetWaitlistEntries methods"""

    def GetWaitlistEntries(self, classScheduleIds,
                           clientIds,
                           waitlistEntryIds,
                           classIds):
        request = self.CreateBasicRequest("GetWaitlistEntries")

        request.ClassScheduleIDs = BasicRequestHelper.FillArrayType(
            self.service, classScheduleIds, "Int")
        request.ClientIDs = BasicRequestHelper.FillArrayType(self.service, clientIds, "String")
        request.WaitlistEntryIDs = BasicRequestHelper.FillArrayType(
            self.service, waitlistEntryIds, "Int")
        request.ClassIDs = BasicRequestHelper.FillArrayType(self.service, classIds, "Int")

        return self.service.service.GetWaitlistEntries(request)

    """RemoveClientsFromClasses methods"""

    def RemoveClientsFromClasses(self, clientIds,
                                 classIds,
                                 test,
                                 sendEmail,
                                 lateCancel):
        request = self.CreateBasicRequest("RemoveClientsFromClasses")

        request.ClientIDs = BasicRequestHelper.FillArrayType(self.service, clientIds, "String")
        request.ClassIDs = BasicRequestHelper.FillArrayType(self.service, classIds, "Int")
        request.Test = test
        request.SendEmail = sendEmail
        request.LateCancel = lateCancel

        return self.service.service.RemoveClientsFromClasses(request)

    """RemoveFromWaitlist methods"""

    def RemoveFromWaitlist(self, waitlistEntryIds):
        request = self.CreateBasicRequest("RemoveFromWaitlist")

        request.WaitlistEntryIDs = BasicRequestHelper.FillArrayType(
            self.service, waitlistEntryIds, "Int")

        return self.service.service.RemoveFromWaitlist(request)

    """UpdateClientVisits methods"""

    def UpdateClientVisits(self, visits,
                           test,
                           sendEmail):
        request = self.CreateBasicRequest("UpdateClientVisits")

        request.Visits = BasicRequestHelper.FillArrayType(self.service, visits, "Visit", "Visit")
        request.Test = test
        request.SendEmail = sendEmail

        return self.service.service.UpdateClientVisits(request)
