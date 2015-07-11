from suds.client import Client
import BasicRequestHelper
from datetime import datetime

class SaleServiceCalls():
    """This class contains examples of consumer methods for each SaleService method."""
    
    """CheckoutShoppingCart Methods"""
    def CheckoutShoppingCart(self, clientId, 
                                   cartItems, 
                                   payments,
                                   cartId=None, 
                                   test=False, 
                                   inStore=False, 
                                   promoCode=None, 
                                   sendEmail=False, 
                                   locationId=None, 
                                   image=None, 
                                   imageFileName=None):
        result = SaleServiceMethods().CheckoutShoppingCart(cartId,
                                                          clientId,
                                                          cartItems,
                                                          payments,
                                                          test,
                                                          inStore,
                                                          promoCode,
                                                          sendEmail,
                                                          locationId,
                                                          image,
                                                          imageFileName)
        return result


    def CreateCartItem(self, arrayToFill,
                             item, 
                             discountAmount=0, 
                             appointments=None,
                             enrollmentIds=None,
                             classIds=None,
                             courseIds=None,
                             visitIds=None,
                             appointmentIds=None,
                             action=None,
                             ID=None,
                             quantity=1):
        """This method is used for creating an element of the CartItems array
           in CheckoutShoppingCart."""
        return SaleServiceMethods().CreateCartItem(arrayToFill,
                                                   item,
                                                   discountAmount,
                                                   appointments,
                                                   enrollmentIds,
                                                   classIds,
                                                   courseIds,
                                                   visitIds,
                                                   appointmentIds,
                                                   action,
                                                   ID,
                                                   quantity)

    def CreateAbstractObject(self, objectType, valueDict):
        """Using this method will append an object of type [objectType] using the
           fields defined in [valueDict] to the end of [arr]. This is for creating
           new Items for CartItems or PaymentInfo in Payments."""
        return SaleServiceMethods().CreateAbstractObject(objectType, valueDict)


    """GetAcceptedCardType Methods"""
    def GetAcceptedCardType(self):
        result = SaleServiceMethods().GetAcceptedCardType()
        return result

    """GetCustomPaymentMethods Methods"""
    def GetCustomPaymentMethods(self):
        result = SaleServiceMethods().GetCustomPaymentMethods()
        return result

    """GetPackages Methods"""
    def GetPackages(self, packageIds=None, sellOnline=False):
        result = SaleServiceMethods().GetPackages(packageIds, sellOnline)
        return result

    """GetProducts Methods"""
    def GetProducts(self, productIds=None,
                          searchText=None,
                          searchDomain=None,
                          categoryIds=None,
                          subCategoryIds=None,
                          sellOnline=False):
        result = SaleServiceMethods().GetProducts(productIds,
                                                  searchText,
                                                  searchDomain,
                                                  categoryIds,
                                                  subCategoryIds,
                                                  sellOnline)
        return result

    """GetSales Methods"""
    def GetSales(self, saleId=None, 
                       startSaleDateTime=datetime.today(), 
                       endSaleDateTime=datetime.today(), 
                       paymentMethodId=None):
        result = SaleServiceMethods().GetSales(saleId, 
                                               startSaleDateTime, 
                                               endSaleDateTime, 
                                               paymentMethodId)
        return result

    """GetServices Methods"""
    def GetServices(self, locationId,
                          programIds=None,
                          sessionTypeIds=None,
                          serviceIds=None,
                          classId=None,
                          classScheduleId=None,
                          sellOnline=False,
                          hideRelatedPrograms=False,
                          staffId=None):
        result = SaleServiceMethods().GetServices(locationId,
                                                  programIds,
                                                  sessionTypeIds,
                                                  serviceIds, 
                                                  classId, 
                                                  classScheduleId, 
                                                  sellOnline,  
                                                  hideRelatedPrograms, 
                                                  staffId)
        return result

    """RedeemSpaFinderWellnessCard Methods"""
    def RedeemSpaFinderWellnessCard(self, cardId, faceAmount, currency, clientId, locationId=None):
        result = SaleServiceMethods().RedeemSpaFinderWellnessCard(cardId,
                                                                  faceAmount,
                                                                  currency,
                                                                  clientId,
                                                                  locationId)
        return result

    """UpdateProducts Methods"""
    def UpdateProducts(self, products, test=False):
        result = SaleServiceMethods().UpdateProducts(products, test)
        return result

    def MatchProductOnlinePricesToPrices(self):
        """This method will set the online price of every product to its normal price."""
        products = SaleServiceMethods().GetProducts(None, None, None, None, None, False).Products.Product

        for currProduct in products:
            currProduct.OnlinePrice = currProduct.Price

        return str(products)

        self.UpdateProducts(products)

    """UpdateServices Methods"""
    def UpdateServices(self, services, test=False):
        result = SaleServiceMethods().UpdateServices(services, test)
        return result

    def MatchServiceOnlinePricesToPricesForLocation(self, locationId):
        services = SaleServiceMethods().GetServices(locationId,
                                                    None,
                                                    None,
                                                    None,
                                                    None,
                                                    None,
                                                    False,
                                                    False,
                                                    None).Services.Service

        for currServ in services:
            currServ.OnlinePrice = currServ.Price

        self.UpdateServices(services)



class SaleServiceMethods():
    """This class contains producer methods for all SaleService methods."""
    wsdl = BasicRequestHelper.BuildWsdlUrl("Sale")
    service = Client(wsdl, location="https://api.mindbodyonline.com/0_5/SaleService.asmx")

    def CreateBasicRequest(self, requestName):
        return BasicRequestHelper.CreateBasicRequest(self.service, requestName)

    """CheckoutShoppingCart methods"""
    def CheckoutShoppingCart(self, cartId,
                                   clientId,
                                   cartItems,
                                   payments,
                                   test,
                                   inStore,
                                   promoCode,
                                   sendEmail,
                                   locationId,
                                   image,
                                   imageFileName):
        request = self.CreateBasicRequest("CheckoutShoppingCart")

        request.CartID = cartId
        request.ClientID = clientId
        request.Test = test
        request.CartItems = BasicRequestHelper.FillArrayType(self.service, cartItems, "CartItem", "CartItem")
        request.InStore = inStore
        request.PromotionCode = promoCode
        request.Payments = BasicRequestHelper.FillArrayType(self.service, payments, "PaymentInfo", "PaymentInfo")
        request.SendEmail = sendEmail
        request.LocationID = locationId
        request.Image = image
        request.ImageFileName = imageFileName

        return self.service.service.CheckoutShoppingCart(request)

    def CreateCartItem(self, arrayToFill,
                             item, 
                             discountAmount, 
                             appointments,
                             enrollmentIds,
                             classIds,
                             courseIds,
                             visitIds,
                             appointmentIds,
                             action,
                             ID,
                             quantity):
        """This method will fill out a CartItem and append it to [arrayToFill]."""
        if arrayToFill == None:
            arrayToFill = []

        cartItem = self.service.factory.create("CartItem")

        if hasattr(item, "Action"):
            delattr(item, "Action")

        cartItem.Item = item
        cartItem.DiscountAmount = discountAmount
        cartItem.Appointments = appointments
        cartItem.EnrollmentIDs = enrollmentIds
        cartItem.ClassIDs = classIds
        cartItem.CourseIDs = courseIds
        cartItem.VisitIDs = visitIds
        cartItem.AppointmentIDs = appointmentIds
        cartItem.Action = action
        cartItem.ID = ID
        cartItem.Quantity = quantity

        arrayToFill.append(cartItem)
        return arrayToFill

    def CreateAbstractObject(self, objectType, valueDict):
        """Using this method will append an object of type [objectType] using the
           fields defined in [valueDict] to the end of [arr]. This is for creating
           new Items for CartItems or PaymentInfo in Payments."""
        return BasicRequestHelper.FillAbstractObject(self.service, objectType, valueDict)

    """GetAcceptedCardType methods"""
    def GetAcceptedCardType(self):
        request = self.CreateBasicRequest("GetAcceptedCardType")

        return self.service.service.GetAcceptedCardType(request)

    """GetCustomPaymentMethods methods"""
    def GetCustomPaymentMethods(self):
        request = self.CreateBasicRequest("GetCustomPaymentMethods")

        return self.service.service.GetCustomPaymentMethods(request)

    """GetPackages methods"""
    def GetPackages(self, packageIds, sellOnline):
        request = self.CreateBasicRequest("GetPackages")

        request.PackageIDs = BasicRequestHelper.FillArrayType(self.service, packageIds, "Int")
        request.SellOnline = sellOnline

        return self.service.service.GetPackages(request)

    """GetProducts methods"""
    def GetProducts(self, productIds, searchText, searchDomain, categoryIds, subCategoryIds, sellOnline):
        request = self.CreateBasicRequest("GetProducts")

        request.ProductIDs = BasicRequestHelper.FillArrayType(self.service, productIds, "String")
        request.SearchText = searchText
        request.SearchDomain = searchDomain
        request.CategoryIDs = BasicRequestHelper.FillArrayType(self.service, categoryIds, "Int")
        request.SubCategoryIDs = BasicRequestHelper.FillArrayType(self.service, subCategoryIds, "Int")
        request.SellOnline = sellOnline

        return self.service.service.GetProducts(request)

    """GetSales methods"""
    def GetSales(self, saleId, startSaleDateTime, endSaleDateTime, paymentMethodId):
        request = self.CreateBasicRequest("GetSales")

        request.SaleID = saleId
        request.StartSaleDateTime = startSaleDateTime
        request.EndSaleDateTime = endSaleDateTime
        request.PaymentMethodID = paymentMethodId

        return self.service.service.GetSales(request)

    """GetServices methods"""
    def GetServices(self, locationId, 
                          programIds,
                          sessionTypeIds,
                          serviceIds, 
                          classId, 
                          classScheduleId, 
                          sellOnline, 
                          hideRelatedPrograms, 
                          staffId):
        request = self.CreateBasicRequest("GetServices")

        request.ProgramIDs = BasicRequestHelper.FillArrayType(self.service, programIds, "Int")
        request.SessionTypeIDs = BasicRequestHelper.FillArrayType(self.service, sessionTypeIds, "Int")
        request.ServiceIDs = BasicRequestHelper.FillArrayType(self.service, serviceIds, "String")
        request.ClassID = classId
        request.ClassScheduleID = classScheduleId
        request.SellOnline = sellOnline
        request.LocationID = locationId
        request.HideRelatedPrograms = hideRelatedPrograms
        request.StaffID = staffId

        return self.service.service.GetServices(request)

    """RedeemSpaFinderWellnessCard methods"""
    def RedeemSpaFinderWellnessCard(self, cardId, faceAmount, currency, clientId, locationId):
        request = self.CreateBasicRequest("RedeemSpaFinderWellnessCard")

        request.CardID = cardId
        request.FaceAmount = faceAmount
        request.Currency = currency
        request.ClientID = clientId
        request.LocationID = locationId

        return self.service.service.RedeemSpaFinderWellnessCard(request)

    """UpdateProducts methods"""
    def UpdateProducts(self, products, test):
        """Note that the only fields supported for update at the moment are
           Price and OnlinePrice."""
        request = self.CreateBasicRequest("UpdateProducts")

        request.Products = products
        request.Test = test

        return self.service.service.UpdateProducts(request)

    """UpdateServices methods"""
    def UpdateServices(self, services, test):
        """Note that the only fields supported for updating at the moment are
           Price and OnlinePrice."""
        request = self.CreateBasicRequest("UpdateServices")

        request.Services = services
        request.Test = test

        return self.service.service.UpdateServices(request)