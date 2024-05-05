
import tkinter as tk
from tkinter import ttk
from page import Page


class Room(Page):
    """
    This class represents a customer
    :Gregory Calderon
    :version 3.0
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
        """
        Sets the rooms available for reservation.

        Args:
            n_rooms (list): List of rooms available for reservation.
            n_checkIn (str): Check-in date for the reservation.
            n_checkOut (str): Check-out date for the reservation.
        """
        self.__rooms = n_rooms
        self.__checkIn = n_checkIn
        self.__checkOut = n_checkOut
      
    def setCustomerEmail(self, n_email):
        """
        Sets the email address of the customer.

        Args:
            n_email (str): The email address of the customer.
        """
        self.__email = n_email
    
    def setCustomerName(self, n_customerName):
        """
        Sets the name of the customer.

        Args:
            n_customerName (str): The name of the customer.
        """
        self.__customerName = n_customerName
           
    def setCustomerId(self, n_customerId):
        """
        Sets the ID of the customer.

        Args:
            n_customerId (str): The ID of the customer.
        """
        self.__customerId = n_customerId
        
    def displayRooms(self):
        """Displays the available rooms for reservation."""
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
        """Populates the room reservation interface with room information."""
        for room in self.__rooms:
            self.roomFrame = tk.Frame(self.innerFrame, borderwidth=2, relief="solid", padx =50, pady=20)
            self.roomFrame.pack(pady=10, fill=tk.X)
            
            roomId = room['roomId']
            roomNum = room['roomNum']
            hotelName = room['hotelName']
            location = room['location']
            cost = room['cost']

            self.roomLabel = tk.Label(self.roomFrame, text=f"Room Id: {roomId}\nRoom Number: {roomNum}\nHotelName: {hotelName}\nLocation: {location}\nCost: {cost}", justify=tk.LEFT)
            self.roomLabel.pack(side=tk.LEFT, padx=10)

            bookRoomsButton = ttk.Button(self.roomFrame, text="Book Now",command=lambda: self.bookRoom(roomId, roomNum, hotelName, location, cost))
            bookRoomsButton.pack(side=tk.RIGHT, padx=10)
        
    def bookRoom(self, roomId, roomNum, hotelName, location, cost):
        """
        Books a room for the customer.

        Args:
            roomId (str): The ID of the room.
            roomNum (str): The room number.
            hotelName (str): The name of the hotel.
            location (str): The location of the hotel.
            cost (float): The cost of the room.
        """
        if self.controller.isLoggedIn == True:
            self.controller.viewReservation.setCustomerName(self.__customerName)
            self.controller.viewReservation.setCustomerId(self.__customerId)
            self.controller.viewReservation.setCustomerEmail(self.__email)
            self.controller.viewReservation.setRoomInfo(roomId, roomNum, hotelName, location, cost, self.__checkIn, self.__checkOut)
            self.controller.isNew=True
            self.controller.viewReservation.updateBtn()
            self.controller.showFrame("ViewReservation")
        else: 
            self.controller.showFrame("Login")
            
    def onCanvasConfigure(self, event):
        """
        Configures the canvas for room display.

        Args:
            event: The event object.
        """
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def clearRooms(self):
        """
        Clear all the widgets related to displaying hotels.
        """
        if hasattr(self, 'roomFrame'):
            self.roomsFrame.destroy()    
        
