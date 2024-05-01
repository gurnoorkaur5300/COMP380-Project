

class Reservation:
    """
    This class represents a Reservation
    :Author: Gregory Calderon and Arameh Baghdassarian
    :Version 1.0
    """
    def __init__(self, customerName=None, room=None, checkInDate=None, checkOutDate=None, paymentID=None):
        """
        Initializes a new Reservation instance.

        Args:
            customerName: The name of the customer.
            room: The room being reserved.
            checkInDate: The date when the customer will check in.
            checkOutDate: The date when the customer will check out.
            paymentID: The payment ID associated with the reservation.
        """
        self.__name = customerName
        self.__room = room
        self.__checkInDate = checkInDate
        self.__checkOutDate = checkOutDate
        self.__paymentID = paymentID

    @property
    def name(self):
        """
        Retrieves the name of the customer.
        
        Returns:
            str: The name of the customer.
        """
        return self.__name

    @name.setter
    def setName(self, name):
        """
        Sets the customer's name.

        Args:
            name: The name of the customer.
        """
        self.__name = name

    @property
    def hotelName(self):
        """
        Retrieves the name of the hotel.

        Returns:
            str: The name of the hotel.
        """
        return self.__hotelName

    @hotelName.setter
    def hotelName(self, hotelName):
        """
        Sets the name of the hotel.

        Args:
            hotelName: The name of the hotel.
        """
        self.__hotelName = hotelName

    @property
    def room(self):
        """
        Retrieves the room number for the reservation.

        Returns:
            int: The room number.
        """
        return self.__room

    @room.setter
    def room(self, room):
        """
        Sets the room number for the reservation.

        Args:
            room: The room number for the reservation.
        """
        self.__room = room
    
    @property
    def checkInDate(self):
        """
        Retrieves the check-in date for the reservation.

        Returns:
            str: The check-in date.
        """
        return self.__checkInDate
    
    @checkInDate.setter
    def setCheckInDate(self, checkInDate):
        """
        Sets the check-in date for the reservation.

        Args:
            checkInDate: The check-in date.
        """
        self.__checkInDate = checkInDate

    @property
    def checkOutDate(self):
        """
        Retrieves the check-out date for the reservation.

        Returns:
            str: The check-out date.
        """
        return self.__checkOutDate
    
    @checkOutDate.setter
    def setCheckOutDate(self, checkOutDate):
        """
        Sets the check-out date for the reservation.

        Args:
            checkOutDate: The check-out date.
        """
        self.__checkOutDate = checkOutDate
