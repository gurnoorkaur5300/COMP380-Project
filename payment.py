import tkinter as tk
from tkinter import messagebox
import hashlib
import re
from reservation import Reservation
from entryBoxUtility import EntryBoxUtility
from paymentClass import PaymentClass
from datetime import datetime
from database import Database
import tkmacosx


class Payment(tk.Toplevel):
    def __init__(self,controller, master=None):
        """
        This class represents the account page.
        :author: Martin Gallegos Cordero
        :version: 2.0
        Initializes the Create window.
        :author: Martin Cordero
        :version: 2.0
        Args:
            controller: The controller object responsible for managing page navigation.
            database: The database object containing user information.
            master: The master widget under which this window is placed.
        """

        self.currentDate = datetime.now()
        super().__init__(master)
        self.controller= controller
        self.database = Database()
        self.title("Payment")
        self.geometry("600x600")
        self.__reserveName = None
        self.__cost = None
        self.__roomId = None
        self.__roomNum = None
        self.__hotelName = None
        self.__location = None
        self.__checkIn = None
        self.__checkOut = None
    
    def setReservationInfo(self, n_customerId, n_customerName, n_roomId, n_roomNum, n_hotelName, n_location, n_cost, n_checkIn, n_checkOut):
        self.__customerId = n_customerId
        self.__reserveName = n_customerName
        self.__hotelName = n_hotelName
        self.__location = n_location
        self.__roomId = n_roomId
        self.__roomNum = n_roomNum
        self.__cost = n_cost
        self.__checkIn = n_checkIn
        self.__checkOut = n_checkOut
        

        #create fields
        self.cardName = tk.Entry(self,width =30, font=("Arial", 20), bg="white", fg="black", insertbackground="black", insertwidth=4 )
        self.cardNumber = tk.Entry(self, width=30,font = ("Arial",20), bg="white", fg="black", insertbackground ="black", insertwidth =4)
        self.securityCode = tk.Entry(self, width =30, font=("Arial", 20), bg="white", fg="black", insertbackground="black", insertwidth =4)
        self.clientAddress = tk.Entry(self, width = 30, font = ("Arial", 20), bg="white", fg="black", insertbackground="black", insertwidth=4)
        self.cityName = tk.Entry(self, width = 30, font = ("Arial", 20), bg="white", fg="black", insertbackground="black", insertwidth =4)
        self.zipCode = tk.Entry(self,width = 30, font = ("Arial",20), bg="white", fg="black", insertbackground="black", insertwidth=4)
        self.expirationDate = tk.Entry(self,width = 30, font = ("Arial",20), bg="white", fg="black", insertbackground="black", insertwidth=4)
        

        self.cardName.insert(0, "Enter full name on card")
        self.cardName.defaultText = "Enter full name on card"
        
        self.cardNumber.insert(0, "Enter card number")
        self.cardNumber.defaultText = "Enter card number"

        self.expirationDate.insert(0, "Enter expiration date")
        self.expirationDate.defaultText = "Enter expiration date"
        
        self.securityCode.insert(0, "Enter security code")
        self.securityCode.defaultText = "Enter security code"
        
        self.clientAddress.insert(0,"Enter address")
        self.clientAddress.defaultText = "Enter address"

        self.cityName.insert(0,"Enter city")
        self.cityName.defaultText = "Enter city"
        
        self.zipCode.insert(0,"Enter zip code")
        self.zipCode.defaultText = "Enter zip code"
        

        #create frame for fields
        entryFrame = tk.Frame(self)
        entryFrame.pack()
        
        #pack entry widgets
        self.cardName.pack(pady=(20,10))
        self.cardNumber.pack(pady=(20,10))
        self.expirationDate.pack(pady=(20,10))
        self.securityCode.pack(pady=(20,10))
        self.clientAddress.pack(pady=(20,10))
        self.cityName.pack(pady=(20,10))
        self.zipCode.pack(pady=20)
   
        
        #create button to submit
        payButton = tkmacosx.Button(
            self, text = "PAY", 
            borderwidth=10, 
            font=("Arial", 22), 
            bg = "white", fg ="black",  
            activeforeground="blue", 
            command= self.getData)
        payButton.pack(side=tk.LEFT, padx=70)

        cancelButton = tkmacosx.Button(
            self,
            text = "CANCEL",
            borderwidth=10,
            font=("Arial", 22),
            bg = "white", 
            fg ="black",  
            activeforeground="blue", 
            command= self.closePayment)
        cancelButton.pack(side=tk.RIGHT, padx=70)


        self.defaultMessages = ["Enter full name on card", "Enter card number","Enter security code", "Enter address", "Enter city", "Enter zip code","Enter expiration date"]

        widgets = [self.cardName, self.cardNumber, self.securityCode, self.clientAddress, self.cityName, self.zipCode, self.expirationDate]

        

        for widget in widgets:
            widget.bind("<FocusIn>", EntryBoxUtility.clearEntries)
            widget.bind("<FocusOut>", EntryBoxUtility.handleEntryFocusOut)

        self.update_idletasks()

            

    def getData(self):
        """
        Retrieves data from entry fields for creating a new user account.

        Returns:
        bool: True if the data is successfully retrieved, False otherwise.
        """
        cardNameValue = self.cardName.get()
        cardNumberValue = self.cardNumber.get()
        expirationDateValue = self.expirationDate.get()
        securityCodeValue = self.securityCode.get() #00/00/0000
        clientAddressValue = self.clientAddress.get() #000-000-0000
        cityNameValue = self.cityName.get().lower()
        zipCodeValue = self.zipCode.get()
     
        

        if not self.validateName(cardNameValue):
            return False
        if not self.validateCardNumber(cardNumberValue):
            #self.resetToDefault(self.userEmail, self.defaultMessages[3])
            return False
        if not self.validateExpirationDate(expirationDateValue):
            return False
        if not self.validateSecurityCode(securityCodeValue):
            return False
        # if not self.validateClientAddress(clientAddress):
        #     return False
        if not self.validateZipCode(zipCodeValue):
            return False
        # if not self.validateCityName(cityName):
        #     self.resetToDefault(self.cityName, self.defaultMessages[4])
        #     return False

        hashCode = hashlib.sha256(securityCodeValue.encode()).hexdigest()
        
       
        newPayment = PaymentClass(cardNameValue, cardNumberValue, expirationDateValue, hashCode, clientAddressValue, zipCodeValue, cityNameValue, self.currentDate, self.__cost)
        self.database.insertPayment(newPayment)
        
        newReservation = Reservation(self.__customerId, self.__reserveName, self.__roomId, self.__roomNum, self.__hotelName, self.__location, self.__cost, self.__checkIn, self.__checkOut)
        
        self.database.insertReservation(newReservation)




    def validateName(self, name):
        """
        Validates the user's first and last name.

        Args:
            firstN (str): The user's first name.
            lastN (str): The user's last name.

        Returns:
            bool: True if both first and last names are provided, False otherwise.
        """
        if not name.strip():
            messagebox.showerror("Error", "Please enter full name")
            return False
        return True

    def validateCardNumber(self, email):
        """
        Validates the user's email address.

        Args:
            email (str): The user's email address.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        pattern = r'^\d{16}$'
        if not re.match(pattern, email):
            messagebox.showerror("Error", "Please enter a valid 16 digit card number")
            self.resetToDefault(self.cardNumber, self.defaultMessages[1])
            return False
        return True
    
    def validateExpirationDate(self, date):
        format = r'^\d{2}-\d{2}$'
        if not re.match(format,date):
            messagebox.showerror("Error", "Please enter a valid date of format MM-YY")
            self.resetToDefault(self.expirationDate, self.defaultMessages[6])
            return False
        return True

    def validateSecurityCode(self, code):
        """
        Validates the user's password.

        Args:
            passwrd (str): The user's password.

        Returns:
            bool: True if the password meets the requirements, False otherwise.
        """
        if len(code) < 3:
            messagebox.showerror("Error", "Code must be 3 digits long")
            self.resetToDefault(self.securityCode, self.defaultMessages[2])
            return False

        if not re.search(r'[0-9]', code) or not re.search(r'\d',code):
            messagebox.showerror("Error", "Code must be only integers")
            self.resetToDefault(self.securityCode, self.defaultMessages[2])
            return False
        return True

    def validateClientAddress(self, address):
        """
        Validates the user's date of birth.

        Args:
            dob (str): The user's date of birth.

        Returns:
            bool: True if the date of birth has the correct format, False otherwise.
        """
        # format = r'^\d+\s+[a-zA-Z]+\s+[a-zA-Z]$'
        format = r'^[a-zA-Z]$'
        if not re.match(format,address):
            messagebox.showerror("Error", "Client address must contain number street name and St/BLVD/RD")
            self.resetToDefault(self.clientAddress, self.defaultMessages[3])
            return False
        return True


    def resetToDefault(self, widget, defaultMessage):
        """
        Reset the entry widget to default text.

        Args:
            widget: The entry widget to reset.
            defaultMessage: The default text to set.
        """
        widget.delete(0, tk.END)
        widget.insert(0, defaultMessage)
        widget.config(show="")  
        widget.bind("<FocusIn>", EntryBoxUtility.clearEntries)
        if widget == self.securityCode:
            widget.bind("<FocusIn>", EntryBoxUtility.handlePasswordFocusIn)
        else:
            widget.bind("<FocusIn>", EntryBoxUtility.handleEntryFocusIn)
        self.focus_set()

    
    def validateCityName(self, city):
        """
        Validates the user's phone number.

        Args:
            phone (str): The user's phone number.

        Returns:
            bool: True if the phone number has the correct format, False otherwise.
        """
        format = r'^[a-zA-Z]$'
        if not re.match(format, city):
            messagebox.showerror("Error", "Phone number should have the format ###-###-####")  
            return False
        return True
    
    def validateZipCode(self, zipCode):
        if len(zipCode) < 5:
            messagebox.showerror("Error", "Code must be 5 digits long")
            self.resetToDefault(self.securityCode, self.defaultMessages[5])
            return False

        if not re.search(r'[0-9]', zipCode) or not re.search(r'\d',zipCode):
            messagebox.showerror("Error", "Code must be 5 integers")
            self.resetToDefault(self.securityCode, self.defaultMessages[5])
            return False
        return True

    #function that displays success message
    def showSuccessMessage(self, title, message):
        messagebox.showerror(title, message)    
     

    def closePayment(self):
        self.destroy() 

# Creates instance of App class and starts GUI   
if __name__=="__main__":
    create = Payment()
    create.mainloop()           
