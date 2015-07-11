try:
  from . import BasicRequestHelper
except:
  import helpers.mbosoap.BasicRequestHelper
  
from suds.client import Client
from datetime import datetime

class StaffServiceCalls():
    """This class contains examples of consumer methods for each StaffService method."""

    """AddOrUpdateStaff Methods"""
    def AddOrUpdateStaff(self, updateAction="AddNew", test=False, staff=None):
        result = StaffServiceMethods().AddOrUpdateStaff(updateAction,
                                                        test,
                                                        staff)
        return(result)

    def EditBioForAllStaff(self, newBio):
        """This function shows how to grab staff to edit, giving a template for
           any similar calls. Modifying the GetStaff call will narrow the 
           affected staff members."""
        staff = StaffServiceMethods().GetStaff(None, 
                                               None, 
                                               None, 
                                               None, 
                                               None, 
                                               None, 
                                               datetime.today(), 
                                               None).StaffMembers.Staff
        for currStaff in staff:
            currStaff.Bio = newBio

        self.AddOrUpdateStaff("Fail", False, staff)
    
    """GetStaff Methods"""
    def GetStaff(self, staffIds=None,
                       staffUsername=None,
                       staffPassword=None,
                       siteIds=None,
                       filters=None,
                       sessionTypeId=None,
                       startDateTime=datetime.today(),
                       locationId=None):
        result = StaffServiceMethods().GetStaff(staffIds,
                                                staffUsername,
                                                staffPassword,
                                                siteIds,
                                                filters,
                                                sessionTypeId,
                                                startDateTime,
                                                locationId)
        return(result)

    def GetStaffWithFiltersAsStrings(self, staffIds=None,
                                           staffUsername=None,
                                           staffPassword=None,
                                           siteIds=None,
                                           filters=None,
                                           sessionTypeId=None,
                                           startDateTime=datetime.today(),
                                           locationId=None):
        result = StaffServiceMethods().GetStaffWithFiltersAsStrings(staffIds,
                                                                    staffUsername,
                                                                    staffPassword,
                                                                    siteIds,
                                                                    filters,
                                                                    sessionTypeId,
                                                                    startDateTime,
                                                                    locationId)
        return result

    """GetStaffImgURL Methods"""
    def GetStaffImgUrl(self, staffId):
        result = StaffServiceMethods().GetStaffImgUrl(staffId)
        return result

    """GetStaffPermissions Methods"""
    def GetStaffPermissions(self, staffId):
        result = StaffServiceMethods().GetStaffPermissions(staffId)
        return result

class StaffServiceMethods():
    """This class contains producer methods for all StaffService methods."""
    wsdl = BasicRequestHelper.BuildWsdlUrl("Staff")
    
    #service = Client(wsdl, retxml=True)
    service = Client(wsdl)

    def CreateBasicRequest(self, requestName):
        return BasicRequestHelper.CreateBasicRequest(self.service, requestName)

    """AddOrUpdateStaff methods"""
    def AddOrUpdateStaff(self, updateAction, test, staff):
        request = self.CreateBasicRequest("AddOrUpdateStaff")

        request.UpdateAction = updateAction
        request.Test = test
        request.Staff = BasicRequestHelper.FillArrayType(self.service, staff, "Staff", "Staff")

        return self.service.service.AddOrUpdateStaff(request)

    """GetStaff methods"""
    def GetStaff(self, staffIds,
                       staffUsername,
                       staffPassword,
                       siteIds,
                       filters,
                       sessionTypeId,
                       startDateTime,
                       locationId):
        request = self.CreateBasicRequest("GetStaff")
        request.StaffIDs = BasicRequestHelper.FillArrayType(self.service, staffIds, "Long")
        request.StaffCredentials = BasicRequestHelper.CreateStaffCredentials(self.service,
                                                                             staffUsername,
                                                                             staffPassword,
                                                                             siteIds)
        request.Filters = BasicRequestHelper.FillArrayType(self.service, filters, "StaffFilter", "StaffFilter")
        request.SessionTypeID = sessionTypeId
        request.StartDateTime = startDateTime
        request.LocationID = locationId

        return self.service.service.GetStaff(request)

    def GetStaffWithFiltersAsStrings(self, staffIds,
                                           staffUsername,
                                           staffPassword,
                                           siteIds,
                                           filters,
                                           sessionTypeId,
                                           startDateTime,
                                           locationId):
        filterEnums = []
        for currFilter in filters:
            filterEnums.append(BasicRequestHelper.GetEnumerable(self.service, "StaffFilter", currFilter))

        return self.GetStaff(staffIds,
                             staffUsername,
                             staffPassword,
                             siteIds,
                             filterEnums,
                             sessionTypeIds,
                             startDateTime,
                             locationId)

    """GetStaffImgURL methods"""
    def GetStaffImgUrl(self, staffId):
        request =  self.CreateBasicRequest("GetStaffImgURL")

        request.StaffID = staffId

        return self.service.service.GetStaffImgURL(request)

    """GetStaffPermissions methods"""
    def GetStaffPermissions(self, staffId):
        request = self.CreateBasicRequest("GetStaffPermissions")

        request.StaffID = staffId

        return self.service.service.GetStaffPermissions(request)