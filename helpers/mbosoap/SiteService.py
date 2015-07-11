try:
  from . import BasicRequestHelper
except:
  import BasicRequestHelper
from suds.client import Client
from datetime import datetime

class SiteServiceCalls():
    """This class contains examples of consumer methods for each SiteService method."""

    """GetActivationCode Methods"""
    def GetActivationCode(self):
        result = SiteServiceMethods().GetActivationCode()
        return result

    """GetLocations Methods"""
    def GetLocations(self):
        result = SiteServiceMethods().GetLocations()
        return result

    """GetPrograms Methods"""
    def GetPrograms(self, scheduleType="All", onlineOnly=False):
        result = SiteServiceMethods().GetPrograms(scheduleType, onlineOnly)
        return result

    """GetRelationships Methods"""
    def GetRelationships(self):
        result = SiteServiceMethods().GetRelationships()
        return result

    """GetResources Methods"""
    def GetResources(self, sessionTypeIds=None,
                           locationId=0,
                           startDateTime=datetime.today(),
                           endDateTime=datetime.today()):
        """Note that 0 is the default value to return from all locations."""
        result = SiteServiceMethods().GetResources(sessionTypeIds,
                                                   locationId,
                                                   startDateTime,
                                                   endDateTime)
        return result

    """GetSessionTypes Methods"""
    def GetSessionTypes(self, programIds=None, onlineOnly=False):
        result = SiteServiceMethods().GetSessionTypes(programIds, onlineOnly)
        return result

    """GetSites Methods"""
    def GetSites(self, searchText=None, relatedSiteId=None):
        result = SiteServiceMethods().GetSites(searchText, relatedSiteId)
        return result

class SiteServiceMethods():
    """This class contains producer methods for all SiteService methods."""
    wsdl = BasicRequestHelper.BuildWsdlUrl("Site")
    service = Client(wsdl)

    def CreateBasicRequest(self, requestName):
        return BasicRequestHelper.CreateBasicRequest(self.service, requestName)

    """GetActivationCode methods"""
    def GetActivationCode(self):
        request = self.CreateBasicRequest("GetActivationCode")

        return self.service.service.GetActivationCode(request)

    """GetLocations methods"""
    def GetLocations(self):
        request = self.CreateBasicRequest("GetLocations")

        return self.service.service.GetLocations(request)

    """GetPrograms methods"""
    def GetPrograms(self, scheduleType, onlineOnly):
        request = self.CreateBasicRequest("GetPrograms")

        request.ScheduleType = BasicRequestHelper.SetEnumerable(self.service, "ScheduleType", scheduleType)
        request.OnlineOnly = onlineOnly

        return self.service.service.GetPrograms(request)

    """GetRelationships methods"""
    def GetRelationships(self):
        request = self.CreateBasicRequest("GetRelationships")

        return self.service.service.GetRelationships(request)

    """GetResources methods"""
    def GetResources(self, sessionTypeIds, locationId, startDateTime, endDateTime):
        request = self.CreateBasicRequest("GetResources")

        request.SessionTypeIDs = BasicRequestHelper.FillArrayType(self.service, sessionTypeIds, "Int")
        request.LocationID = locationId
        request.StartDateTime = startDateTime
        request.EndDateTime = endDateTime

        return self.service.service.GetResources(request)

    """GetSessionTypes methods"""
    def GetSessionTypes(self, programIds, onlineOnly):
        request = self.CreateBasicRequest("GetSessionTypes")

        request.ProgramIDs = BasicRequestHelper.FillArrayType(self.service, programIds, "Int")
        request.OnlineOnly = onlineOnly

        return self.service.service.GetSessionTypes(request)

    """GetSites methods"""
    def GetSites(self, searchText, relatedSiteId):
        request = self.CreateBasicRequest("GetSites")

        request.SearchText = searchText
        request.RelatedSiteID = relatedSiteId

        return self.service.service.GetSites(request)