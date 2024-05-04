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
    :author: Arameh Baghdasarian
    :version: 1.0

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
        self.__roomId = None
        self.__roomNum = None
        self.__hotelName = None
        self.__location = None
        self.__cost = None
        
        self.__checkIn = None
        self.__checkOut = None
        
   
        
        self.isNew =True
        
        self.reservationLabel = tk.Label(self, text="", font=("Arial", 24),justify=tk.LEFT)
        self.reservationLabel.pack(fill=tk.X, pady=15)
        
    # @property
    # def isNew(self):
    #     return self.isNew

    @property
    def customerName(self):
        return self.__name  
    
  
    def setCustomerName(self, n_customerName):
        """Set the customer's name."""
        self.__name = n_customerName
        
    def setCustomerId(self, n_customerId):
        self.__id = n_customerId
    

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
            
        confirmBtnState = "active" if self.isNew else "disabled"
        cancelBtnState = "disabled" if self.isNew else "active"
            
        confirmButton = tk.Button(
                self,
                text="Confirm",
                borderwidth=0,
                font=(
                    "Arial",
                    35),fg="black",
                activeforeground="blue",
                command=lambda: self.showPayment(),state=cancelBtnState)
        confirmButton.place(relx=0.3, rely=.8, anchor=tk.CENTER)
        

        cancelButton = tk.Button(
                self,
                text="Cancel",
                borderwidth=0,
                font=(
                    "Arial",
                    35),
                fg="black",
                activeforeground="blue",
                command=lambda: self.cancelReservation(),state= confirmBtnState)
        cancelButton.place(relx=0.7, rely=.8, anchor=tk.CENTER)

    def showPayment(self):
        """
        Opens the payment page.
        """
        payWindow = Payment(self) 
        # print("the id is: ", self.__id)
        payWindow.setReservationInfo(self.__id, self.__name, self.__roomId, self.__roomNum, self.__hotelName, self.__cost, self.__location, self.__checkIn, self.__checkOut)
         

    def cancelReservation(self):
        """
        Opens the cancel reservation window
        """
        # CancelReservation(self, database)     
    

    

# def confirmReservation(self):
#     """
#     Confirms the customer's reservation and populates the reservation class

#     call the payment window and pass reservation to his page
#     """

#         # def showPayment(self, database):
#         #     """
#         #     Opens the payment page.
#         #     """
#         #     if self.isUserVar.get() == 1:
#         #         Payment(self, database)
#         #     else:
#         #         messagebox.showerror("ERROR", "Unauthorized Action")


#         # newReservation = Reservation(
#         #     customerName=self.customer.name,
#         #     room=self.room,
#         #     checkInDate=self.home.checkinDate,
#         #     checkOutDate=self.home.checkoutDate,
            
#         # )

    
       

#     # def cancelReservation(self):
#         """
#         Cancels the current reservation process (return to home page) and removes 
#         reservation info from database(if the reservation has already been made)
        
#         are you sure you want to cancel this reservation if the reservation exists

#         call deleteReservation

#         call reset function to delete summary data
#         """     
#         # self.controller.showFrame("Home")


#     def setSummary(self, n_customer):
#         """
#         Sets the reservation summary information that will be displayed.

#         Args:
#             n_customer: The customer object whose account information will be displayed.
#         """
#         self.customer = n_customer
        
#         self.columnconfigure(0, weight=1)
#         self.columnconfigure(1, weight=0)

         
#         infoBox = tk.Frame(self)
#         infoBox.grid(row=0,column=0,padx=(35,35), pady=75,sticky="ew")


#         labelsInfo = [
#         ("Name:", self.customer.name),
#         ("Location:", self.room.location),
#         ("Room:", self.room.roomNum),
#         ("Check-in Date:", self.home.checkinDate),
#         ("Check-out Date:", self.home.checkoutDate),
#         ("Cost:", self.room.cost),
#         ]

#         self.infoLabels = []

#         for i, (labelText, value) in enumerate(labelsInfo):
#             label = tk.Label(infoBox, text=labelText, font=("Arial", 24, "bold"), bg="white", fg="black")
#             label.grid(row=i, column=0, padx=15, sticky="e")

#             valueLabel = tk.Label(infoBox, text=value, bg="white", fg="black", anchor="w", font=("Ariel",24), width=50)
#             valueLabel.grid(row=i, column=1, pady=15, sticky="w")
#             self.infoLabels.append(valueLabel)


#         # confirmButton = tk.Button(
#         #         self,
#         #         text="Confirm",
#         #         borderwidth=0,
#         #         font=(
#         #             "Arial",
#         #             32),fg="black",
#         #         activeforeground="blue",
#         #         command=self.confirmReservation)
#         # confirmButton.place(relx=0.3, rely=.8, anchor=tk.CENTER)
        

#         # cancelButton = tk.Button(
#         #         self,
#         #         text="Cancel Booking",
#         #         borderwidth=0,
#         #         font=(
#         #             "Arial",
#         #             16),
#         #         fg="black",
#         #         activeforeground="blue",
#         #         command=self.cancelReservation)
#         # cancelButton.place(relx=0.7, rely=.8, anchor=tk.CENTER)
        