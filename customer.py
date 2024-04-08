import tkinter as tk


class Customer:
    def __init__(self, n_name, n_email, n_dob, n_reservations=[]):
        self.__name= n_name
        self.__email= n_email
        self.__dob= n_dob
        self.__reservations = n_reservations if n_reservations is not None else []

    #set Cx name
    def setName(self, n_name):
        self.__name = n_name

    #set Cx email
    def setEmail(self, n_email):
        self.__email = n_email

    #set Cx dob
    def setDob(self, n_dob):
        self.__dob = n_dob

        
    #add reservation to a list of reservations
    def addReservations(self, n_reservation):
        self.__reservations.append(n_reservation)
    
    #return Cx name
    def getName(self):
        return self.__name

    #return Cx email
    def getEmail(self):
        return self.__email

    #get Cx date of birth
    def getDob(self):
        return self.__dob

    #get Cx reservation
    def getReservations(self):
        return self.__reservations
