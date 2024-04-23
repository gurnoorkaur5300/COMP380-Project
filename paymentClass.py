class PaymentClass:
    def __init__(self, n_cardName=None, n_cardNum=None, n_securityCode=None, n_clientAddress=None, n_cityName=None, n_zipCode=None, n_expDate=None):
        
        #private variables that velong to payment class
        self.__name = n_cardName
        self.__number = n_cardNum
        self.__code = n_securityCode
        self.__address = n_clientAddress
        self.__city = n_cityName
        self.__zip = n_zipCode
        self.__date = n_expDate

    #getters and setters for the class PaymentClass
    @property
    def name(self):
        
        return self.__name

    @name.setter
    def setName(self, n_name):
        
        self.name = n_name
    
    @property
    def number(self):
       
        return self.__number

    @number.setter
    def setcardNumber(self, n_cardNumber):
        
        self.number = n_cardNumber

    @property
    def code(self):
      
        return self.__code

    @code.setter
    def setcardCode(self, n_securityCode):
      
        self.code = n_securityCode

    @property
    def address(self):
        
        return self.__address

    @address.setter
    def setAddress(self, n_clientAddress):
      
        self.address = n_clientAddress

    @property
    def city(self):
        
        return self.__city

    @city.setter
    def setcityName(self, n_cityName):
      
        self.city = n_cityName

    @property
    def zip(self):
        
        return self.__zip

    @zip.setter
    def setzipCode(self, n_zipCode):
        
        self.zip = n_zipCode             

    @property
    def date(self):
        
        return self.__date

    @date.setter
    def setexpDate(self, n_expDate):
       
        self.date = n_expDate

