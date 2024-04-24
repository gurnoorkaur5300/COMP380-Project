class PaymentClass:
    """
    This class represents the account page.
        :author: Martin Gallegos Cordero
        :version: 2.0
    Represents a payment transaction.

    Attributes:
        name (str): Name on the card.
        number (str): Card number.
        code (str): Security code.
        address (str): Client address.
        city (str): City name.
        zip (str): ZIP code.
        date (str): Expiration date.

    Methods:
        setName(name: str) -> None: Set the name on the card.
        setcardNumber(number: str) -> None: Set the card number.
        setcardCode(code: str) -> None: Set the security code.
        setAddress(address: str) -> None: Set the client address.
        setcityName(city: str) -> None: Set the city name.
        setzipCode(zip: str) -> None: Set the ZIP code.
        setexpDate(date: str) -> None: Set the expiration date.
    """
    def __init__(self, n_cardName=None, n_cardNum=None, n_securityCode=None, n_clientAddress=None, n_cityName=None, n_zipCode=None, n_expDate=None):
        """
        Initialize a PaymentClass object.

        Args:
            n_cardName (str, optional): Name on the card.
            n_cardNum (str, optional): Card number.
            n_securityCode (str, optional): Security code.
            n_clientAddress (str, optional): Client address.
            n_cityName (str, optional): City name.
            n_zipCode (str, optional): ZIP code.
            n_expDate (str, optional): Expiration date.
        """
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
        """
        Return the name on the card.
        """
        return self.__name

    @name.setter
    def setName(self, n_name):
        """
        Set the name on the card.

        Args:
            name (str): Name on the card.
        """
        self.name = n_name
    
    @property
    def number(self):
        """
        Return the number on the card.
        """
        return self.__number

    @number.setter
    def setcardNumber(self, n_cardNumber):
        """
        Set the card number.

        Args:
            number (str): Card number.
        """
        
        self.number = n_cardNumber

    @property
    def code(self):
        """
        Return the code on the card.
        """
        return self.__code

    @code.setter
    def setcardCode(self, n_securityCode):
        """
        Set the security code.

        Args:
            code (str): Security code.
        """
      
        self.code = n_securityCode

    @property
    def address(self):
        """
        Return the address on the card.
        """
        return self.__address

    @address.setter
    def setAddress(self, n_clientAddress):
        """
        Set the client address.

        Args:
            address (str): Client address.
        """
      
        self.address = n_clientAddress

    @property
    def city(self):
        """
        Return the city on the card.
        """
        return self.__city

    @city.setter
    def setcityName(self, n_cityName):
        """
        Set the city name.

        Args:
            city (str): City name.
        """
      
        self.city = n_cityName

    @property
    def zip(self):
        """
        Return the zip code on the card.
        """
        return self.__zip

    @zip.setter
    def setzipCode(self, n_zipCode):
        """
        Set the ZIP code.

        Args:
            zip (str): ZIP code.
        """
        
        self.zip = n_zipCode             

    @property
    def date(self):
        """
        Return the date on the card.
        """
        return self.__date

    @date.setter
    def setexpDate(self, n_expDate):
        """
        Set the expiration date.

        Args:
            date (str): Expiration date.
        """
       
        self.date = n_expDate


