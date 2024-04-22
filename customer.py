class Customer:
    """
    This class represents a customer
    :Gregory Calderon
    :version 1.1
    """

    def __init__(self, n_name=None, n_email=None, n_dob=None,n_phone= None, n_hashPass=None, n_reservations=None):

        """
        Constructs a customer

        :param n_name: (Optional) The name of the customer..
        :type n_name: str
        :param n_email: (Optional) The email address of the customer. 
        :type n_email: str
        :param n_dob: (Optional) The date of birth of the customer in the format 'MM/DD/YYYY'.
        :type n_dob: str
        :param n_phone: (Optional) The phone number of the customer. 
        :type n_phone: str
        :param n_reservations: (Optional) List of reservations made by the customer. 
        :type n_reservations: list, optional
        """
        self.__name= n_name
        self.__email= n_email
        self.__dob= n_dob
        self.__phoneNumber = n_phone
        self.__hashPass = n_hashPass
        self.__reservations = n_reservations if n_reservations is not None else []

    @property
    def name(self):
        """str: The name of the customer."""
        return self.__name

    @name.setter
    def setName(self, n_name):
        """
        Sets the customer name.
        :param n_name: Customer's name.
        :type n_name: str
        """
        self.__name = n_name

   
    @property
    def email(self):
        """str: The email address of the customer."""
        return self.__email

    @email.setter
    def setEmail(self, n_email):
        """  
        Sets the customer email.
        :param n_email: Customer's email.
        :type n_email: str
        """
        self.__email = n_email
 
    @property
    def phoneNumber(self):
        """str: The phone number of the customer."""
        return self.__phoneNumber
    
    @phoneNumber.setter
    def setPhone(self, n_phone):
        """  
        Sets the customer Phone.
        :param n_Phone: Customer's Phone number.
        :type n_Phone: str
        """
        self.__phoneNumber = n_phone
    
    @property
    def dob(self):
        """str: The date of birth of the customer."""
        return self.__dob
    
    @dob.setter
    def setDob(self, n_dob):
        """
        Sets the customer dob.
        :param n_dob: Customer's dob.
        :type n_dob: str
        """
        self.__dob = n_dob

    @property
    def reservations(self):
        """list: List of reservations made by the customer."""
        return self.__reservations
    

    def addReservations(self, n_reservation):
        """
        Adds to the the customer reservation list.
        :param n_reservation: Customer's new reservation.
        :type n_reservation: str
        """  
        self.__reservations.append(n_reservation)
   

    @property
    def hashPass(self):
        """str: The hash of the customer's password."""
        return self.__hashPass