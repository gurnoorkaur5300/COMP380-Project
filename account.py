import tkinter as tk
import tkmacosx
from page import Page
from entryBoxUtility import EntryBoxUtility 


class Account(Page):
    """
    This class represents the account page.
    :author: Gregory Calderon
    :version: 2.0

    Attributes:
        parent: The parent widget to which the account page belongs.
        database: The database object containing customer information.
        controller: The controller object responsible for managing page navigation.
        customer: The customer object whose account information is displayed.

    Methods:
        setCustomer(n_customer): Sets the customer whose account information will be displayed.
    """
    def __init__(self,parent, database, controller, loginPage = None, customer=None):
        """
        Initializes the Account object.

        Args:
            parent: The parent widget to which the account page belongs.
            database: The database object containing customer information.
            controller: The controller object responsible for managing page navigation.
            customer: The customer object whose account information is displayed. Default is None.
        """
        super().__init__(parent,controller)
        self.controller = controller
        self.database = database 
        self.customer = customer
        self.loginPage = loginPage

    def clearAccountPage(self):
        """
        Clears the account page by resetting the text of displayed information.
        """
        """
        Logs out the user.
        """
        self.clearLoginEntryBoxes()

    def clearLoginEntryBoxes(self):
        """
        Clears the login entry boxes.
        """     
        if hasattr(self.controller, 'loginPage') and callable(getattr(self.controller.loginPage, 'reset', None)):
            self.controller.loginPage.reset()

    def setCustomer(self, n_customer):
        """
        Sets the customer whose account information will be displayed.

        Args:
            n_customer: The customer object whose account information will be displayed.
        """
        self.customer = n_customer
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

         
        infoBox = tk.Frame(self)
        infoBox.grid(row=0,column=0,padx=(35,35), pady=75,sticky="ew")


        labelsInfo = [
        ("Id:", self.customer.id),
        ("Name:", self.customer.name),
        ("Email:", self.customer.email),
        ("Phone:", self.customer.phoneNumber),
        ("DOB:", self.customer.dob)
        ]

        self.infoLabels = []

        for i, (labelText, value) in enumerate(labelsInfo):
            label = tk.Label(infoBox, text=labelText, font=("Arial", 24, "bold"), bg="white", fg="black")
            label.grid(row=i, column=0, padx=15, sticky="e")

            valueLabel = tk.Label(infoBox, text=value, bg="white", fg="black", anchor="w", font=("Ariel",24), width=50)
            valueLabel.grid(row=i, column=1, pady=15, sticky="w")
            self.infoLabels.append(valueLabel)

       

        reservationFrame = tk.Frame(self)
        reservationFrame.grid(row=1, column=0, padx=(35,35), sticky="ew")
        
        reservationsLabel = tk.Label(reservationFrame, text="Reservations:", font=("Arial", 24, "bold"), bg="white", fg="black")
        reservationsLabel.grid(row=0, column=0, sticky="e", padx=15)

        for i, reservation in enumerate(self.customer.reservations):
            reservationButton = tk.Button(reservationFrame, text=reservation, command=lambda: self.showReservation(reserveId), anchor="center", bg="white", fg="black", font=(18), width=10)
            reservationButton.grid(row= 0, column=i+1, sticky='w')
            reserveId = reservation.split(":")[0].strip()
        
    def showReservation(self, reserveId):
        reservationInfoString = self.database.getResInfo(reserveId)
        
        # self.controller.showFrame("viewReservation")
        
    def reset(self):
        """
        Resets the administrative page.
        """
        #clear spreadsheet
        self.clearAccountPage()
        #reset global variables
        # global isLoggedIn, isAdmi
        
        if self.controller.isAdmin:
            self.controller.showFrame("Admin")
        elif not self.controller.isAdmin:
            self.controller.showFrame("Home")
        #     self.controller.isLoggedIn = False
        # self.controller.isAdmin = False