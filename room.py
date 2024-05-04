
import tkinter as tk
from tkinter import ttk
from page import Page


class Room(Page):
    """
    This class represents a customer
    :Gregory Calderon
    :version 1.0
    """
    def __init__(self, parent, controller, n_rooms=None, n_checkIn=None, n_checkOut=None, n_customer=None):
        super().__init__(parent, controller)
        self.controller = controller
        """
        Initializes a Room object with the provided attributes.

        Args:
            n_hotelName (str, optional): The name of the hotel. Defaults to None.
            n_roomNum (str, optional): The room number. Defaults to None.
            n_location (str, optional): The location of the hotel. Defaults to None.
            n_cost (float, optional): The cost of the room. Defaults to None.
        """  
        self.__rooms = n_rooms
        self.__checkIn = n_checkIn
        self.__checkOut = n_checkOut
        
    def setRooms(self, n_rooms, n_checkIn, n_checkOut):
        self.__rooms = n_rooms
        self.__checkIn = n_checkIn
        self.__checkOut = n_checkOut
      
        
    def setCustomer(self, n_customer):
        self.__customer = n_customer
        
    def displayRooms(self):
        self.roomsFrame = tk.Frame(self, bg='white')
        self.roomsFrame.pack(fill=tk.BOTH, expand=True)
        
        self.contentFrame = tk.Frame(self.roomsFrame, bg='white')
        self.contentFrame.pack(fill=tk.BOTH, expand=True,side=tk.LEFT)
        
        self.canvas = tk.Canvas(self.contentFrame, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.onCanvasConfigure)
       
        self.innerFrame = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window((0, 0), window=self.innerFrame, anchor="nw")


        scrollbar = ttk.Scrollbar(self.roomsFrame, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.populateRooms()
    
    def populateRooms(self):  
        for room in self.__rooms:
            self.roomFrame = tk.Frame(self.innerFrame, borderwidth=2, relief="solid", padx =50, pady=20)
            self.roomFrame.pack(pady=10, fill=tk.X)
            
            
            # print(room)
            # photoPath = room['photoLink']
            # try:
            #     image = Image.open(photoPath)
            #     image = image.resize((100, 100))
            #     img = ImageTk.PhotoImage(image)
            #     img_label = tk.Label(self.roomFrame, image=img)
            #     img_label.image = img
            #     img_label.pack(side=tk.LEFT, padx=10)
            # except Exception as e:
            #     print("Error opening or resizing image:", e)
            
            # self.roomInfo = {
            #     'roomId': room['roomId'],
            #     'roomNum': room['roomNum'],
            #     'hotelName': room['hotelName'],
            #     'location': room['location'],
            #     'cost': room['cost']
            # }
            
            roomId = room['roomId']
            roomNum = room['roomNum']
            hotelName = room['hotelName']
            location = room['location']
            cost = room['cost']

            # self.roomInfo = f"Room Id: {room['roomId']}\nRoom Number: {room['roomNum']}\nHotelName: {room['hotelName']}\nLocation: {room['location']}\nCost: {room['cost']}"
            self.roomLabel = tk.Label(self.roomFrame, text=f"Room Id: {roomId}\nRoom Number: {roomNum}\nHotelName: {hotelName}\nLocation: {location}\nCost: {cost}", justify=tk.LEFT)
            self.roomLabel.pack(side=tk.LEFT, padx=10)

            bookRoomsButton = ttk.Button(self.roomFrame, text="Book Now",command=lambda: self.bookRoom(roomId, roomNum, hotelName, location, cost))
            bookRoomsButton.pack(side=tk.RIGHT, padx=10)
        
    def bookRoom(self, roomId, roomNum, hotelName, location, cost):
        if self.controller.isLoggedIn == True:
            
            print(self.__customer)
          
            self.controller.viewReservation.setCustomerName(self.__customer)
            self.controller.viewReservation.setCustomerId(self.__customer)
            self.controller.viewReservation.setRoomInfo(roomId, roomNum, hotelName, location, cost, self.__checkIn, self.__checkOut)
            self.controller.showFrame("ViewReservation")
        else: 
            self.controller.showFrame("Login")
            
            # ViewReservation()
    def onCanvasConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        
    # @property
    # def hotelName(self):
    #     """str: The name of the hotel the room is in."""
    #     return self.__hotelName

    # @hotelName.setter
    # def hotelName(self, n_hotelName):
    #     """
    #     Sets the hotel name that the room is in.
    #     :param n_name: hotel's name.
    #     :type n_name: str
    #     """
    #     self.__hotelName = n_hotelName

    # @property
    # def roomNum(self):
    #     """str: The room number."""
    #     return self.__roomNum

    # @roomNum.setter
    # def roomNum(self, n_roomNum):
    #     """
    #     Sets the room number.
    #     :param n_name: room number.
    #     :type n_name: int
    #     """
    #     self.__roomNum = n_roomNum


    # @property
    # def location(self):
    #     """str: The number of people that the room is rated to sleep."""
    #     return self.__location

    # @location.setter
    # def location(self, n_location):
    #     """
    #     Sets the number of people that the room is rated to sleep.
    #     :param n_location: number of people that the room is rated to sleep.
    #     :type n_location: str
    #     """
    #     self.__location = n_location

    # @property
    # def cost(self):
    #     """str: The cost of the room."""
    #     return self.__cost

    # @cost.setter
    # def cost(self, n_cost):
    #     """
    #     Sets the cost of the room.
    #     :param n_name: cost of the room.
    #     :type n_name: float
    #     """
    #     self.__cost = n_cost

    # @staticmethod
    # def genRoomNum(n_roomNum):
    #     if n_roomNum is None:
    #         """Generate a rooom number."""
    #         return random.randint(100,999)

    