import tkinter as tk
from page import Page
from customer import Customer


class Account(Page):
    def __init__(self,parent,controller, customer):
        super().__init__(parent,controller)
        Page.__init__(self,parent, controller)
        self.customer = customer
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        infoBox = tk.Frame(self)
        infoBox.grid(row=0,column=0, pady=5,sticky="ew")
        
        userNameLabel = tk.Label(infoBox, text="Name:", font=("Arial", 18, "bold"), bg="white", fg="black")
        userNameLabel.grid(row=0, column=0, padx=15,sticky="e")

        userNameLabel = tk.Label(infoBox,text=self.customer.name, bg="white", fg="black", anchor="w", width=50)
        userNameLabel.grid(row=0, column=1, pady=15, sticky="w")
        
        userEmailLabel = tk.Label(infoBox, text="Email:", font=("Arial", 18, "bold"), bg="white", fg="black")
        userEmailLabel.grid(row=1, column=0, padx=15,sticky="e")

        userEmailLabel = tk.Label(infoBox,text=self.customer.email, bg="white", fg="black", anchor="w", width=50)
        userEmailLabel.grid(row=1, column=1, pady=15, sticky="w")
        
        userDOBLabel = tk.Label(infoBox, text="DOB:", font=("Arial", 18, "bold"), bg="white", fg="black")
        userDOBLabel.grid(row=2, column=0, padx=15,sticky="e")

        userDOBLabel = tk.Label(infoBox,text=self.customer.dob, bg="white", fg="black", anchor="w", width=15)
        userDOBLabel.grid(row=2, column=1, pady=15, sticky="w")
        
        userReservationsLabel = tk.Label(infoBox, text="Reservations:", font=("Arial", 18, "bold"), bg="white", fg="black")
        userReservationsLabel.grid(row=4, column=0, padx=15,sticky="e")
        
        
        for i, reservation in enumerate(customer.reservations):
            userReservationsLabel = tk.Label(infoBox, text=reservation, anchor="w", bg="white", fg="black", width=50)
            userReservationsLabel.grid(row=i+4, column=1, pady=10, sticky="w")

        
    