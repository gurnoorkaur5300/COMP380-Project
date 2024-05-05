import tkinter as tk
# import tkmacosx
from page import Page
# from entryBoxUtility import EntryBoxUtility 
# from login import Login
# from room import Room
# from home import Home

from payment import Payment
from tkinter import messagebox
from entryBoxUtility import EntryBoxUtility 
# from cancelReservation import CancelReservation


class ViewReservation(Page):
    """
    This class represents the viewReservation page.
    :author: Arameh Baghdasarian and Gregory Calderon
    :version: 3.0 

    Attributes:
        parent: The parent widget to which the page belongs.
        database: The database object containing customer information.
        controller: The controller object responsible for managing page navigation.
        customer: The customer object whose account information is displayed.

    Methods:
        setCustomer(n_customer): Sets the customer whose account information will be displayed.
    """
    def __init__(self,parent, database, controller):
        """
        Initializes the reservation page object.

        Args:
            parent: The parent widget to which the account page belongs.
            database: The database object containing customer information.
            controller: The controller object responsible for managing page navigation.
            customer: The customer object whose account information is displayed. Default is None.
        """
        super().__init__(parent,controller)
        self.controller = controller
        self.database = database 
    
        self.__id = None
        self.__name = None
        self.__email = None
        self.__roomId = None
        self.__roomNum = None
        self.__hotelName = None
        self.__location = None
        self.__cost = None
        self.__reserveId = None
        self.__checkIn = None
        self.__checkOut = None
        
   
        
       
        
        self.reservationLabel = tk.Label(self, text="", font=("Arial", 24),justify=tk.LEFT)
        self.reservationLabel.pack(fill=tk.X, pady=15)
        

    @property
    def customerName(self):
        return self.__name  
    
  
    def setCustomerName(self, n_customerName):
        """Set the customer's name."""
        self.__name = n_customerName
        
    def setCustomerId(self, n_customerId):
        self.__id = n_customerId
        
    def setReserveId(self, n_reserveId):
        self.__reserveId = n_reserveId
        
    def setCustomerEmail(self, n_customerEmail):
        self.__email = n_customerEmail
    

    def setRoomInfo(self, n_roomId, n_roomNum, n_hotelName, n_location, n_cost, n_checkIn, n_checkOut):
        """Set the room information."""
        self.__roomId = n_roomId
        self.__roomNum = n_roomNum
        self.__hotelName = n_hotelName
        self.__location = n_location
        self.__cost = n_cost
        self.__checkIn = n_checkIn
        self.__checkOut = n_checkOut
        
        
        self.updateReservationLabel()
    
    @property
    def checkIn(self):
        return self.__checkIn
    
    @property
    def checkOut(self):
        return self.__checkOut
    
    def updateReservationLabel(self):
        """Update the reservation label with the current room information."""
        roomText = f"Name: {self.__name}\nRoom Id: {self.__roomId}\nRoom Number: {self.__roomNum}\nHotel Name: {self.__hotelName}\nLocation: {self.__location}\nCheck In: {self.__checkIn}\nCheck Out: {self.__checkOut}\nCost: {self.__cost}\n"
        self.reservationLabel.config(text=roomText)
            
        self.confirmButton = tk.Button(
                self,
                text="Confirm",
                borderwidth=0,
                font=(
                    "Arial",
                    35),fg="black",
                activeforeground="blue",
                command=self.showPayment)
        self.confirmButton.place(relx=0.3, rely=.8, anchor=tk.CENTER)
        

        self.cancelButton = tk.Button(
                self,
                text="Cancel",
                borderwidth=0,
                font=(
                    "Arial",
                    35),
                fg="black",
                activeforeground="blue",
                command=lambda: self.cancelReservation(self.__reserveId))
        self.cancelButton.place(relx=0.7, rely=.8, anchor=tk.CENTER)

        self.updateBtn()

    def updateBtn(self):
        confirmBtnState = "active" if self.controller.isNew else "disabled"
        cancelBtnState = "disabled" if self.controller.isNew else "active"

        self.confirmButton.config(state=confirmBtnState)
        self.cancelButton.config(state=cancelBtnState)

    def showPayment(self):
        """
        Opens the payment page.
        """
        payWindow = Payment(self, self.controller.accountPage) 
        # print("the id is: ", self.__id)
        payWindow.setReservationInfo(self.__id, self.__name, self.__email, self.__roomId, self.__roomNum, self.__hotelName, self.__cost, self.__location, self.__checkIn, self.__checkOut)
         

    def cancelReservation(self, reserveId):
        """
        Opens the cancel reservation window
        """
        self.controller.accountPage.clearReserveFrame()
        self.database.deleteReservation(reserveId, self.__email)
        
        self.controller.accountPage.loadReservation()
            
    def reset(self):
        """
        Resets the ViewReservation page by clearing all the information displayed on the page.
        """
        self.__id = None
        self.__name = None
        self.__email = None
        self.__roomId = None
        self.__roomNum = None
        self.__hotelName = None
        self.__location = None
        self.__cost = None
        self.__reserveId = None
        self.__checkIn = None
        self.__checkOut = None

        # Clear the reservation label
        self.reservationLabel.config(text="")

        # Clear the confirm and cancel buttons
        if hasattr(self, 'confirmButton'):
            self.confirmButton.destroy()
        if hasattr(self, 'cancelButton'):
            self.cancelButton.destroy()

        # Update button states
        self.updateBtn()
    

    

