 

class Customer:
    """
    This class represents a customer
    :Gregory Calderon
    :version 1.0
    """

    def __init__(self, n_name="none", n_email="none@gnot.com", n_dob="01/01/0000",n_phone= "000-000-0000", n_hashPass=None, n_reservations=None):

        """
        Constructs a customer

        :param n_name: (Optional) The name of the customer. Default is None.
        :type n_name: str
        :param n_email: (Optional) The emial address of the customer. Default is none@gnot.com.
        :type n_email str
        :param n_dob: (Optional) The date of birth of the customer in the format 'MM/DD/YYYY'. Default is "01/01/0000".
        :type n_dob: str
        :param n_reservations: (Optional) List of reservations made by the customer. Defaults to an empty list.
        :type n_reservations: list, optional
        """
        self.__name= n_name
        self.__email= n_email
        self.__dob= n_dob
        self.__phoneNumber = n_phone
        self.__hashPass = n_hashPass
        self.__reservations = n_reservations if n_reservations is not None else []

    #set Cx name
    def setName(self, n_name):
        """
        Sets the customer name.
        :param n_name: Customer's name.
        :type n_name: str
        """
        self.name = n_name

   
    #set Cx email
    def setEmail(self, n_email):
        """  
        Sets the customer email.
        :param n_email: Customer's email.
        :type n_email: str
        """
        self.email = n_email
        
    #set Cx email
    def setPhone(self, n_phone):
        """  
        Sets the customer Phone.
        :param n_Phone: Customer's Phone number.
        :type n_Phone: str
        """
        self.phoneNumber = n_phone
    
    #set Cx dob
    def setDob(self, n_dob):
        """
        Sets the customer dob.
        :param n_dob: Customer's dob.
        :type n_dob: str
        """
        self.dob = n_dob

      
    #add reservation to a list of reservations
    def addReservations(self, n_reservation):
        """
        Adds to the the customer reservation list.
        :param n_reservation: Customer's new reservation.
        :type n_reservation: str
        """  
        self.__reservations.append(n_reservation)
   

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def dob(self):
        return self.__dob

    @property
    def phoneNumber(self):
        return self.__phoneNumber

    @property
    def hashPass(self):
        return self.__hashPass

    @property
    def reservations(self):
        return self.__reservations
