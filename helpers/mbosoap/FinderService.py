import BasicRequestHelper
from suds.client import Client
from datetime import datetime


class FinderServiceCalls():

    """This class contains examples of consumer methods for each StaffService method."""

    """AddOrUpdateFinderUsers Methods"""

    def AddOrUpdateFinderUsers(self, partnerId,
                               finderUsers,
                               updateAction="AddNew",
                               test=False,
                               noClientEmail=False):
        result = FinderServiceMethods().AddOrUpdateFinderUsers(partnerId,
                                                               finderUsers,
                                                               updateAction,
                                                               test,
                                                               noClientEmail)
        return result

    """FinderCheckoutShoppingCart Methods"""

    def FinderCheckoutShoppingCart(self, partnerId,
                                   latitude,
                                   longitude,
                                   paymentInfo,
                                   test=False,
                                   noClientEmail=False,
                                   mbfClassId=None,
                                   mbfSessionTypeId=None,
                                   sessionDateTime=datetime.today(),
                                   staffId=0,
                                   saveCCInfo=False,
                                   spaFinderWellnessCard=None):
        result = FinderServiceMethods().FinderCheckoutShoppingCart(partnerId,
                                                                   latitude,
                                                                   longitude,
                                                                   paymentInfo,
                                                                   test,
                                                                   noClientEmail,
                                                                   mbfClassId,
                                                                   mbfSessionTypeId,
                                                                   sessionDateTime,
                                                                   staffId,
                                                                   saveCCInfo,
                                                                   spaFinderWellnessCard)
        return result

    def FinderCheckoutShoppingCartWithPaymentAsDictionary(self, partnerId,
                                                          latitude,
                                                          longitude,
                                                          paymentType,
                                                          paymentDict,
                                                          test=False,
                                                          noClientEmail=False,
                                                          mbfClassId=None,
                                                          mbfSessionTypeId=None,
                                                          sessionDateTime=datetime.today(),
                                                          staffId=0,
                                                          saveCCInfo=False,
                                                          spaFinderWellnessCard=None):
        """This method will take a payment type and dictionary and create a PaymentInfo
           from it before running FinderCheckoutShoppingCart."""
        newPayment = BasicRequestHelper.FillAbstractObject(paymentType, paymentDict)
        self.FinderCheckoutShoppingCart(partnerId,
                                        latitude,
                                        longitude,
                                        newPayment,
                                        test,
                                        noClientEmail,
                                        mbfClassId,
                                        mbfSessionTypeId,
                                        sessionDateTime,
                                        staffId,
                                        saveCCInfo,
                                        spaFinderWellnessCard)

    """GetBusinessLocationsWithinRadius methods"""

    def GetBusinessLocationsWithinRadius(self, latitude=None,
                                         longitude=None,
                                         radius=None,
                                         locationId=None,
                                         text=None,
                                         sortOption="Alphabetical",
                                         domain="ClassInfo"):
        result = FinderServiceMethods().GetBusinessLocationsWithinRadius(latitude,
                                                                         longitude,
                                                                         radius,
                                                                         locationId,
                                                                         text,
                                                                         sortOption,
                                                                         domain)
        return result

    """GetClassesWithinRadius Methods"""

    def GetClassesWithinRadius(self, latitude,
                               longitude,
                               radius,
                               startDateTime=datetime.today(),
                               endDateTime=datetime.today(),
                               locationId=0,
                               classId=0,
                               text=None,
                               sortOption="Chronological",
                               domain="ClassInfo",
                               ipaddress=None):
        result = FinderServiceMethods().GetClassesWithinRadius(latitude,
                                                               longitude,
                                                               radius,
                                                               startDateTime,
                                                               endDateTime,
                                                               locationId,
                                                               classId,
                                                               text,
                                                               sortOption,
                                                               domain,
                                                               ipaddress)
        return result

    """GetFinderUser Methods"""

    def GetFinderUser(self, email, password=None, partnerId=None):
        result = FinderServiceMethods().GetFinderUser(email, password, partnerId)
        return result

    """GetSessionTypesWithinRadius Methods"""

    def GetSessionTypesWithinRadius(self, latitude,
                                    longitude,
                                    radius,
                                    locationId=None,
                                    sessionTypeId=None,
                                    text=None,
                                    sortOption="Chronological",
                                    domain="SessionTypeInfo",
                                    ipaddress=None,
                                    sessionsPerLocation=3):
        result = FinderServiceMethods().GetSessionTypesWithinRadius(latitude,
                                                                    longitude,
                                                                    radius,
                                                                    locationId,
                                                                    sessionTypeId,
                                                                    text,
                                                                    sortOption,
                                                                    domain,
                                                                    ipaddress,
                                                                    sessionsPerLocation)
        return result

    """SendFinderUserNewPassword Methods"""

    def SendFinderUserNewPassword(self, email):
        result = FinderServiceMethods().SendFinderUserNewPassword(email)
        return result


class FinderServiceMethods():

    """This class contains producer methods for all FinderService methods."""
    wsdl = BasicRequestHelper.BuildWsdlUrl("Finder")
    service = Client(wsdl)

    def CreateBasicRequest(self, requestName):
        """Since FinderService is designed to poll across multiple sites, we use
           SiteID 0 to poll across all sites."""
        return BasicRequestHelper.CreateBasicRequest(self.service, requestName, [0])

    """AddOrUpdateFinderUsers methods"""

    def AddOrUpdateFinderUsers(self, partnerId,
                               finderUsers,
                               updateAction,
                               test,
                               noClientEmail):
        request = self.CreateBasicRequest("AddOrUpdateFinderUsers")

        request.PartnerID = partnerId
        request.FinderUsers = finderUsers
        request.UpdateAction = updateAction
        request.Test = test
        request.NoClientEmail = noClientEmail

        return self.service.service.AddOrUpdateFinderUsers(request)

    """FinderCheckoutShoppingCart methods"""

    def FinderCheckoutShoppingCart(self, partnerId,
                                   latitude,
                                   longitude,
                                   paymentInfo,
                                   test,
                                   noClientEmail,
                                   mbfClassId,
                                   mbfSessionTypeId,
                                   sessionDateTime,
                                   staffId,
                                   saveCCInfo,
                                   spaFinderWellnessCard):
        request = self.CreateBasicRequest("FinderCheckoutShoppingCart")

        request.Test = test
        request.NoClientEmail = noClientEmail
        request.MBFClassID = mbfClassId
        request.MBFSessionTypeID = mbfSessionTypeId
        request.SessionDateTime = sessionDateTime
        request.StaffID = staffId
        request.PartnerID = partnerId
        request.SearchLatitude = latitude
        request.SearchLongitude = longitude
        request.SaveCCInfo = saveCCInfo
        request.SpaFinderWellnessCard = spaFinderWellnessCard
        request.PaymentInfo = paymentInfo

        return self.service.service.FinderCheckoutShoppingCart(request)

    def CreatePaymentInfo(self, paymentType, paymentDict):
        """This will generate and return a usable PaymentInfo"""
        return BasicRequestHelper.FillAbstractObject(self.service, paymentType, paymentDict)

    """GetBusinessLocationsWithinRadius methods"""

    def GetBusinessLocationsWithinRadius(self, latitude,
                                         longitude,
                                         radius,
                                         locationId,
                                         text,
                                         sortOption,
                                         domain):
        request = self.CreateBasicRequest("GetBusinessLocationsWithinRadius")

        request.SearchLatitude = latitude
        request.SearchLongitude = longitude
        request.SearchRadius = radius
        request.SearchLocationID = locationId
        request.SearchText = text
        request.SortOption = sortOption
        request.SearchDomain = domain

        return self.service.service.GetBusinessLocationsWithinRadius(request)

    """GetClassesWithinRadius methods"""

    def GetClassesWithinRadius(self, latitude,
                               longitude,
                               radius,
                               startDateTime,
                               endDateTime,
                               locationId,
                               classId,
                               text,
                               sortOption,
                               domain,
                               ipaddress):
        request = self.CreateBasicRequest("GetClassesWithinRadius")

        request.SearchLatitude = latitude
        request.SearchLongitude = longitude
        request.SearchRadius = radius
        request.StartDateTime = startDateTime
        request.EndDateTime = endDateTime
        request.SearchLocationID = locationId
        request.SearchClassID = classId
        request.SearchText = text
        request.SortOption = sortOption
        request.SearchDomain = domain
        request.IPAddress = ipaddress

        return self.service.service.GetClassesWithinRadius(request)

    """GetFinderUser methods"""

    def GetFinderUser(self, email, password, partnerId):
        request = self.CreateBasicRequest("GetFinderUser")

        request.Email = email
        request.Password = password
        request.PartnerID = partnerId

        return self.service.service.GetFinderUser(request)

    """GetSessionTypesWithinRadius methods"""

    def GetSessionTypesWithinRadius(self, latitude,
                                    longitude,
                                    radius,
                                    locationId,
                                    sessionTypeId,
                                    text,
                                    sortOption,
                                    domain,
                                    ipaddress,
                                    sessionsPerLocation):
        request = self.CreateBasicRequest("GetSessionTypesWithinRadius")

        request.SearchLatitude = latitude
        request.SearchLongitude = longitude
        request.SearchRadius = radius
        request.SearchLocationID = locationId
        request.SearchSessionTypeID = sessionTypeId
        request.SearchText = text
        request.SortOption = sortOption
        request.SearchDomain = domain
        request.IPAddress = ipaddress
        request.SessionsPerLocation = sessionsPerLocation

        return self.service.service.GetSessionTypesWithinRadius(request)

    """SendFinderUserNewPassword methods"""

    def SendFinderUserNewPassword(self, email):
        request = self.CreateBasicRequest("SendFinderUserNewPassword")

        request.Email = email

        return self.service.service.SendFinderUserNewPassword(request)
