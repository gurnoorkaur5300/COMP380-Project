import tkinter as tk
from tkinter import messagebox
import hashlib
import re
from customer import Customer
from entryBoxUtility import EntryBoxUtility

class Payment(tk.Toplevel):
    def __init__(self,controller, database, master=None):
        """
        Initializes the Create window.

        Args:
            controller: The controller object responsible for managing page navigation.
            database: The database object containing user information.
            master: The master widget under which this window is placed.
        """
        super().__init__(master)
        self.controller= controller
        self.database = database 
        self.title("Payment")
        self.geometry("600x600")

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

        self.expirationDate(0, "Enter expiration date")
        self.expirationDate.defaultText = "Enter expiration date"
        
        self.securityCode(0, "Enter security code")
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
        self.cardName.pack(pady=(20,20))
        self.cardNumber.pack(pady=(20,20))
        self.expirationDate.pack(pady=(20,20))
        self.securityCode.pack(pady=(20,20))
        self.clientAddress.pack(pady=(20,20))
        self.cityName.pack(pady=(20,20))
        self.zipCode.pack(pady=(20,20))
   

        #create button to submit
        payButton = tk.Button(self, text = "PAY", borderwidth=10, font=("Arial", 22), bg = "white", fg ="black",  activeforeground="blue", command= self.getData)
        payButton.pack(padx = 200, side = "left")

        cancelButton = tk.Button(self, text = "CANCEL", borderwidth=10, font=("Arial", 22), bg = "white", fg ="black",  activeforeground="blue", command= self.getData)
        cancelButton.pack(padx = 200, side = "right")


        self.defaultMessages = ["Enter full name on card", "Enter card number","Enter security code", "Enter address", "Enter city", "Enter zip code","Enter expiration date"]

        widgets = [self.cardName, self.cardNumber, self.securityCode, self.clientAddress, self.cityName, self.zipCode, self.expirationDate]

        for widget in widgets:
            widget.bind("<FocusIn>", EntryBoxUtility.clearEntries)
            widget.bind("<FocusOut>", EntryBoxUtility.handleEntryFocusOut)


        # Special handling for password-related widgets
        # self.userPassword.bind("<FocusIn>", EntryBoxUtility.handlePasswordFocusIn)
        # self.userPasswordConfirm.bind("<FocusIn>", EntryBoxUtility.handlePasswordFocusIn)


        self.update_idletasks()

            

    def getData(self):
        """
        Retrieves data from entry fields for creating a new user account.

        Returns:
        bool: True if the data is successfully retrieved, False otherwise.
        """
        cardName = self.cardName.get()
        cardNumber = self.cardNumber.get()
        expirationDate = self.expirationDate.get()
        securityCode= self.securityCode.get() #00/00/0000
        clientAddress = self.clientAddress.get() #000-000-0000
        cityName = self.cityName.get().lower()
        zipCode = self.zipCode.get()

        if not self.validateName(cardName):
            return False
        if not self.validateCardNumber(cardNumber):
            #self.resetToDefault(self.userEmail, self.defaultMessages[3])
            return False
        if not self.validateExpirationDate(expirationDate):
            return False
        if not self.validateSecurityCode(securityCode):
            return False
        if not self.validateClientAddress(clientAddress):
            return False
        if not self.validateZipCode(zipCode):
            return False
        if not self.validateCityName(cityName):
            self.resetToDefault(self.cityName, self.defaultMessages[4])
            return False

        # name = cardName
        # hashPasswrd = hashlib.sha256(securityCode.encode()).hexdigest()

        #newPayment = Customer(name, email, dob, phone, hashPasswrd)

        

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
        format = r'^[0-9]+[a-zA-Z]+[a-zA-Z]$'
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
            messagebox.showerror("Error", "Code must be 3 digits long")
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
     

    def closeCreate(self):
        self.destroy() 

# Creates instance of App class and starts GUI   
if __name__=="__main__":
    create = Payment()
    create.mainloop()           
