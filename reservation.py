from customer import Customer
from room import Room

class Reservation:
    """
    This class represents a Reservation
    :Author: Gregory Calderon and Arameh Baghdassarian
    :Version 1.0
    """
    def __init__(self, customerName=None, room=None, checkInDate=None, checkOutDate=None, paymentID=None):
        """
        Initialize a new Reservation instance.

        :param name: The customer making the reservation
        :type name: str
        :param room: The room being reserved
        :type room: int
        :param checkInDate: The date when the customer will check in
        :type checkInDate: str
        :param checkOutDate: The date when the customer will check out
        :type checkOutDate: str
        """

        self.__name = customerName
        self.__room = room
        self.__checkInDate = checkInDate
        self.__checkOutDate = checkOutDate
        self.__paymentID = paymentID

    @property
    def name(self):
        """str: The name of the customer."""
        return self.__name

    @name.setter
    def setName(self, name):
        """
        Sets the customer name.
        :param name: Customer's name.
        :type name: str
        """
        self.name = name

   
    @property
    def hotelName(self):
        """str: The name of the Hotel where the room is being booked."""
        return self.__hotelName

    @hotelName.setter
    def hotelName(self, hotelName):
        """  
        Sets the hotelName.
        :param hotelName: Hotel's name.
        :type hotelName: str
        """
        self.hotelName = hotelName
 
    @property
    def room(self):
        """int: The room number for the customer."""
        return self.__room
    
    @room.setter
    def room(self, room):
        """  
        Sets the room number.
        :param room: Customer's room.
        :type room: int
        """
        self.room = room
    
    @property
    def checkInDate(self):
        """str: The date of the customer's check-in."""
        return self.__checkInDate
    
    @checkInDate.setter
    def setDob(self, checkInDate):
        """
        Sets the customer check-in date.
        :param checkInDate: Customer's check in.
        :type checkInDate: str
        """
        self.dob = checkInDate

    @property
    def checkOutDate(self):
        """str: The date of the customer's check-out."""
        return self.__checkOutDate
    
    @checkOutDate.setter
    def setDob(self, checkOutDate):
        """
        Sets the customer check-out date.
        :param checkOutDate: Customer's check out.
        :type checkOutDate: str
        """
        self.dob = checkOutDate
