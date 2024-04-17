import random

class Room:
    """
    This class represents a customer
    :Gregory Calderon
    :version 1.0
    """
    def __init__(self, n_hotelName=None, n_roomNum=None, n_location=None, n_cost=None):
          
        self.__hotelName = n_hotelName
        self.__roomNum= n_roomNum
        self.__location = n_location
        self.__cost = n_cost

    @property
    def hotelName(self):
        """str: The name of the hotel the room is in."""
        return self.__hotelName

    @hotelName.setter
    def hotelName(self, n_hotelName):
        """
        Sets the hotel name that the room is in.
        :param n_name: hotel's name.
        :type n_name: str
        """
        self.__hotelName = n_hotelName

    @property
    def roomNum(self):
        """str: The room number."""
        return self.__roomNum

    @roomNum.setter
    def roomNum(self, n_roomNum):
        """
        Sets the room number.
        :param n_name: room number.
        :type n_name: int
        """
        self.__roomNum = n_roomNum


    @property
    def location(self):
        """str: The number of people that the room is rated to sleep."""
        return self.__location

    @location.setter
    def location(self, n_location):
        """
        Sets the number of people that the room is rated to sleep.
        :param n_location: number of people that the room is rated to sleep.
        :type n_location: str
        """
        self.__location = n_location

    @property
    def cost(self):
        """str: The cost of the room."""
        return self.__cost

    @cost.setter
    def cost(self, n_cost):
        """
        Sets the cost of the room.
        :param n_name: cost of the room.
        :type n_name: float
        """
        self.__cost = n_cost

    @staticmethod
    def genRoomNum(n_roomNum):
        if n_roomNum is None:
            """Generate a rooom number."""
            return random.randint(100,999)

    