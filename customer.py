import tkinter as tk


class Customer:
    def __init__(self, name, email, dob, reservations=[]):
        self.name= name
        self.email= email
        self.dob= dob
        self.reservations = reservations if reservations is not None else []
        
    #add reservation to a list of reservations
    def addReservations(self, reservation):
        self.reservations.append(reservation)
        
    def getCustomer(self):
        return self.name
