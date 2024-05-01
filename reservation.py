

class Reservation:
    """
    This class represents a Reservation
    :Author: Gregory Calderon and Arameh Baghdassarian
    :Version 1.0
    """
    def __init__(self, n_customerName=None, n_roomId=None, n_roomNum=None, n_hotelName=None, n_location=None, n_cost=None, n_checkIn=None, n_checkOut=None):
        """
        Initializes a new Reservation instance.

        Args:
            customerName: The name of the customer.
            room: The room being reserved.
            checkInDate: The date when the customer will check in.
            checkOutDate: The date when the customer will check out.
            paymentID: The payment ID associated with the reservation.
        """
        self.__name = n_customerName
        self.__roomId = n_roomId
        self.__roomNum = n_roomNum
        self.__hotelName = n_hotelName
        self.__location = n_location
        self.__cost = n_cost
        self.__checkIn=n_checkIn
        self.__checkOut= n_checkOut
        # self.__roomInfo = None
    
 
    # @property 
    # def roomInfo(self):
    #     return self.__roomInfo
        
    # @roomInfo.setter
    # def roomInfo(self, n_roomInfo):
    #     self.__roomInfo = n_roomInfo
        
    # @property  
    # def roomId(self):
    #     return self.__roomInfo.get('roomId')
    # @property
    # def roomNum(self):
    #     return self.__roomInfo.get('roomNum')
    # @property
    # def hotelName(self):
    #     return self.__roomInfo.get('hotelName')
    # @property
    # def location(self):
    #     return self.roomInfo.get('location')
    # @property
    # def getCost(self):
    #     return self.roomInfo.get('Cost')

    @property
    def name(self):
        """
        Retrieves the name of the customer.
        
        Returns:
            str: The name of the customer.
        """
        return self.__name

    # @name.setter
    # def setName(self, name):
    #     """
    #     Sets the customer's name.

    #     Args:
    #         name: The name of the customer.
    #     """
    #     self.__name = name

    @property
    def hotelName(self):
        """
        Retrieves the name of the hotel.

        Returns:
            str: The name of the hotel.
        """
        return self.__hotelName

    # @hotelName.setter
    # def hotelName(self, hotelName):
    #     """
    #     Sets the name of the hotel.

    #     Args:
    #         hotelName: The name of the hotel.
    #     """
    #     self.__hotelName = hotelName

    @property
    def roomNum(self):
        """
        Retrieves the room number for the reservation.

        Returns:
            int: The room number.
        """
        return self.__roomNum

    # @roomNum.setter
    # def roomNum(self, n_roomNum):
    #     """
    #     Sets the room number for the reservation.

    #     Args:
    #         room: The room number for the reservation.
    #     """
    #     self.__roomNum = n_roomNum
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
