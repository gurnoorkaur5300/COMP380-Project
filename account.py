import tkinter as tk
from page import Page
from entryBoxUtility import EntryBoxUtility 
from login import Login


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
    def __init__(self,parent, database, controller, customer=None):
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
        if hasattr(self.controller, 'loginPage') and hasattr(self.controller.loginPage, 'reset'):
            self.controller.loginPage.reset(self.controller.loginPage.userEmail, "Enter username")
            self.controller.loginPage.reset(self.controller.loginPage.userPassword, "Enter password")        

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
        infoBox.grid(row=0,column=0, pady=5,sticky="ew")


        labelsInfo = [
        ("Name:", self.customer.name),
        ("Email:", self.customer.email),
        ("Phone:", self.customer.phoneNumber),
        ("DOB:", self.customer.dob)
        ]

        self.infoLabels = []

        for i, (label_text, value) in enumerate(labelsInfo):
            label = tk.Label(infoBox, text=label_text, font=("Arial", 18, "bold"), bg="white", fg="black")
            label.grid(row=i, column=0, padx=15, sticky="e")

            valueLabel = tk.Label(infoBox, text=value, bg="white", fg="black", anchor="w", width=50)
            valueLabel.grid(row=i, column=1, pady=15, sticky="w")
            self.infoLabels.append(valueLabel)  # Append label objects to info_labels list

        
        reservationsLabel = tk.Label(infoBox, text="Reservations:", font=("Arial", 18, "bold"), bg="white", fg="black")
        reservationsLabel.grid(row=len(labelsInfo), column=0, padx=15, sticky="e")

        
        for i, reservation in enumerate(self.customer.reservations):
            reservationLabel = tk.Label(infoBox, text=reservation, anchor="w", bg="white", fg="black", width=50)
            reservationLabel.grid(row=i + len(labelsInfo) + 1, column=1, pady=10, sticky="w")
            self.infoLabels.append(reservationLabel)  
