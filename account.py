import tkinter as tk
from page import Page


class Account(Page):
    def __init__(self,parent, database, controller, customer=None):
        super().__init__(parent,controller)
        self.controller = controller
        self.database = database 
        self.customer = customer

    def setCustomer(self, n_customer):
        self.customer = n_customer
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        # create a grid frame to display info 
        infoBox = tk.Frame(self)
        infoBox.grid(row=0,column=0, pady=5,sticky="ew")
        
        #column 0 shows data type to be displayed on that row
        userNameLabel = tk.Label(infoBox, text="Name:", font=("Arial", 18, "bold"), bg="white", fg="black")
        userNameLabel.grid(row=0, column=0, padx=15,sticky="e")
        
        userEmailLabel = tk.Label(infoBox, text="Email:", font=("Arial", 18, "bold"), bg="white", fg="black")
        userEmailLabel.grid(row=1, column=0, padx=15,sticky="e")

        userPhoneLabel = tk.Label(infoBox, text="Phone:", font=("Arial", 18, "bold"), bg="white", fg="black")
        userPhoneLabel.grid(row=1, column=0, padx=15,sticky="e")
        
        userDOBLabel = tk.Label(infoBox, text="DOB:", font=("Arial", 18, "bold"), bg="white", fg="black")
        userDOBLabel.grid(row=2, column=0, padx=15,sticky="e")
        
        userReservationsLabel = tk.Label(infoBox, text="Reservations:", font=("Arial", 18, "bold"), bg="white", fg="black")
        userReservationsLabel.grid(row=4, column=0, padx=15,sticky="e")

        #column 1 is data of customer
        userNameLabel = tk.Label(infoBox,text=self.customer.name, bg="white", fg="black", anchor="w", width=50)
        userNameLabel.grid(row=0, column=1, pady=15, sticky="w")

        userEmailLabel = tk.Label(infoBox,text=self.customer.email, bg="white", fg="black", anchor="w", width=50)
        userEmailLabel.grid(row=1, column=1, pady=15, sticky="w")

        userPhoneLabel = tk.Label(infoBox,text=self.customer.phoneNumber, bg="white", fg="black", anchor="w", width=50)
        userPhoneLabel.grid(row=1, column=1, pady=15, sticky="w")

        userDOBLabel = tk.Label(infoBox,text=self.customer.dob, bg="white", fg="black", anchor="w", width=15)
        userDOBLabel.grid(row=2, column=1, pady=15, sticky="w")
        
        for i, reservation in enumerate(self.customer.reservations):
            userReservationsLabel = tk.Label(infoBox, text=reservation, anchor="w", bg="white", fg="black", width=50)
            userReservationsLabel.grid(row=i+4, column=1, pady=10, sticky="w")

        
    