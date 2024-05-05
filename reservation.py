

class Reservation:
    """
    This class represents a Reservation
    :Author: Gregory Calderon and Arameh Baghdassarian
    :Version 1.0
    """
    def __init__(self, n_customerId=None, n_customerName=None, n_roomId=None, n_roomNum=None, n_hotelName=None, n_cost=None, n_location=None, n_checkIn=None, n_checkOut=None):
        """
        Initializes a new Reservation instance.

        Args:
            customerName: The name of the customer.
            room: The room being reserved.
            checkInDate: The date when the customer will check in.
            checkOutDate: The date when the customer will check out.
            paymentID: The payment ID associated with the reservation.
        """
        self.__customerId = n_customerId
        self.__name = n_customerName
        self.__roomId = n_roomId
        self.__roomNum = n_roomNum
        self.__hotelName = n_hotelName
        self.__location = n_location
        self.__cost = n_cost
        self.__checkIn=n_checkIn
        self.__checkOut= n_checkOut

    @property
    def location(self):
        return self.__location
   

    @property
    def customerId(self):
        """
        Retrieves the id of the customer.
        
        Returns:
            str: The id of the customer.
        """
        return self.__customerId

    @property
    def name(self):
        """
        Retrieves the name of the customer.
        
        Returns:
            str: The name of the customer.
        """
        return self.__name


    @property
    def hotelName(self):
        """
        Retrieves the name of the hotel.

        Returns:
            str: The name of the hotel.
        """
        return self.__hotelName

    @property
    def roomNum(self):
        """
        Retrieves the room number for the reservation.

        Returns:
            int: The room number.
        """
        return self.__roomNum

    @property
    def roomId(self):
        return self.__roomId
    
    @property
    def cost(self):
        return self.__cost
    
    @property
    def checkIn(self):
        """
        Retrieves the check-in date for the reservation.

        Returns:
            str: The check-in date.
        """
        return self.__checkIn
    
    @checkIn.setter
    def setCheckIn(self, n_checkIn):
        """
        Sets the check-in date for the reservation.

        Args:
            checkIn: The check-in date.
        """
        self.__checkIn= n_checkIn

    @property
    def checkOut(self):
        """
        Retrieves the check-out date for the reservation.

        Returns:
            str: The check-out date.
        """
        return self.__checkOut
    
    @checkOut.setter
    def setCheckOut(self, n_checkOutDate):
        """
        Sets the check-out date for the reservation.

        Args:
            checkOut: The check-out date.
        """
        self.__checkOut = n_checkOutDate
