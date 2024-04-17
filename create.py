import tkinter as tk
from tkinter import messagebox
import hashlib
import re
from customer import Customer
from entryBoxUtility import EntryBoxUtility

class Create(tk.Toplevel):
    """
    This class represents the window for creating a new user account.
    :author: Gregory Calderon and Martin Gallegos Cordero 

    Attributes:
        controller: The controller object responsible for managing page navigation.
        database: The database object containing user information.
        master: The master widget under which this window is placed.

    Methods:
        passwordMatch(): Verifies if Password and Confirm Password match.
        getData(): Retrieves data from entry fields for creating a new user account.
        validateName(firstN, lastN): Validates the user's first and last name.
        validateEmail(email): Validates the user's email address.
        validatePassword(passwrd): Validates the user's password.
        validateDOB(dob): Validates the user's date of birth.
        validatePhoneNumber(phone): Validates the user's phone number.
        closeCreate(): Closes the create account window.
    """
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
        self.title("Create Account")
        self.geometry("600x600")

        #create fields
        self.userName = tk.Entry(self,width =30, font=("Arial", 20), bg="white", fg="black", insertbackground="black", insertwidth=4 )
        self.userLastName = tk.Entry(self, width=30,font = ("Arial",20), bg="white", fg="black", insertbackground ="black", insertwidth =4)
        self.userDOB = tk.Entry(self, width =30, font=("Arial", 20), bg="white", fg="black", insertbackground="black", insertwidth =4)
        self.userEmail = tk.Entry(self, width = 30, font = ("Arial", 20), bg="white", fg="black", insertbackground="black", insertwidth=4)
        self.userPhone = tk.Entry(self, width = 30, font = ("Arial", 20), bg="white", fg="black", insertbackground="black", insertwidth =4)
        self.userPassword = tk.Entry(self,width = 30, font = ("Arial",20), bg="white", fg="black", insertbackground="black", insertwidth=4)
        self.userPasswordConfirm = tk.Entry(self, width =30, font =("Arial", 20), bg="white", fg="black", insertbackground="black", insertwidth=4)
        self.securityWord = tk.Entry(self, font = ("Arial", 20), bg ="white", fg ="black")

        self.userName.insert(0, "Enter first name")
        self.userName.defaultText = "Enter first name"
        
        self.userLastName.insert(0, "Enter last name")
        self.userLastName.defaultText = "Enter last name"
        
        self.userDOB.insert(0, "Enter DOB")
        self.userDOB.defaultText = "Enter DOB"
        
        self.userEmail.insert(0,"Enter email")
        self.userEmail.defaultText = "Enter email"

        self.userPhone.insert(0,"Enter Phone")
        self.userPhone.defaultText = "Enter Phone"
        
        self.userPassword.insert(0,"Enter password")
        self.userPassword.defaultText = "Enter password"
        
        self.userPasswordConfirm.insert(0,"Confirm password")
        self.userPasswordConfirm.defaultText = "Confirm password"

        #create frame for fields
        entryFrame = tk.Frame(self)
        entryFrame.pack()
        
        #pack entry widgets
        self.userName.pack(pady=(20,20))
        self.userLastName.pack(pady=(20,20))
        self.userDOB.pack(pady=(20,20))
        self.userEmail.pack(pady=(20,20))
        self.userPhone.pack(pady=(20,20))
        self.userPassword.pack(pady=(20,20))
        self.userPasswordConfirm.pack(pady =(20,20))
   

        #create button to submit
        submitButton = tk.Button(self, text = "SUBMIT", borderwidth=10, font=("Arial", 22), bg = "white", fg ="black",  activeforeground="blue", command= self.getData)
        submitButton.pack(padx = 200, side = "left")


        self.defaultMessages = ["Enter first name", "Enter last name","Enter DOB", "Enter email", "Enter Phone", "Enter password", "Confirm password"]

        widgets = [self.userName, self.userLastName, self.userDOB, self.userEmail, self.userPhone, self.userPassword, self.userPasswordConfirm]

        for widget in widgets:
            widget.bind("<FocusIn>", EntryBoxUtility.clearEntries)
            widget.bind("<FocusOut>", EntryBoxUtility.handleEntryFocusOut)


        # Special handling for password-related widgets
        self.userPassword.bind("<FocusIn>", EntryBoxUtility.handlePasswordFocusIn)
        self.userPasswordConfirm.bind("<FocusIn>", EntryBoxUtility.handlePasswordFocusIn)


        self.update_idletasks()


      #Create function that veryfies if Password and Confirm Password match
    def passwordMatch(self):
        """
        Checks if the entered passwords match.

        Returns:
        bool: True if passwords match, False otherwise.
        """
        passWord = self.userPassword.get()
        passWordConfirma = self.userPasswordConfirm.get()
        if passWord != passWordConfirma:
            self.showSuccessMessage("Error", "Passwords do not match, Press OK and try again")
            self.resetToDefault(self.userPassword, self.defaultMessages[5])
            self.resetToDefault(self.userPasswordConfirm, self.defaultMessages[6])
            return False
        return True
            

    def getData(self):
        """
        Retrieves data from entry fields for creating a new user account.

        Returns:
        bool: True if the data is successfully retrieved, False otherwise.
        """
        firstName = self.userName.get()
        lastName = self.userLastName.get()
        dob = self.userDOB.get() #00/00/0000
        phone = self.userPhone.get() #000-000-0000
        email = self.userEmail.get().lower()
        passwrd = self.userPassword.get()

        if not self.validateName(firstName, lastName):
            return False
        if not self.validateEmail(email):
            #self.resetToDefault(self.userEmail, self.defaultMessages[3])
            return False
        if not self.validatePassword(passwrd):
            return False
        if not self.validateDOB(dob):
            return False
        if not self.validatePhoneNumber(phone):
            self.resetToDefault(self.userPhone, self.defaultMessages[4])
            return False

        name = firstName + " " + lastName
        hashPasswrd = hashlib.sha256(passwrd.encode()).hexdigest()

        newCustomer = Customer(name, email, dob, phone, hashPasswrd)


    ##turn into If else statement to clear the email if the email already exists
        if self.database.insertCustomer(newCustomer):
            self.closeCreate()
        else: 
            self.resetToDefault(self.userEmail, self.defaultMessages[3])   
        return True
        

    def validateName(self, firstN, lastN):
        """
        Validates the user's first and last name.

        Args:
            firstN (str): The user's first name.
            lastN (str): The user's last name.

        Returns:
            bool: True if both first and last names are provided, False otherwise.
        """
        if not firstN.strip() or not lastN.strip():
            messagebox.showerror("Error", "Please enter both a first and last name")
            return False
        return True

    def validateEmail(self, email):
        """
        Validates the user's email address.

        Args:
            email (str): The user's email address.

        Returns:
            bool: True if the email address is valid, False otherwise.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            messagebox.showerror("Error", "Please enter a valid email address")
            self.resetToDefault(self.userEmail, self.defaultMessages[3])
            return False
        return True

    def validatePassword(self, passwrd):
        """
        Validates the user's password.

        Args:
            passwrd (str): The user's password.

        Returns:
            bool: True if the password meets the requirements, False otherwise.
        """
        if len(passwrd) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long")
            self.resetToDefault(self.userPassword, self.defaultMessages[5])
            self.resetToDefault(self.userPasswordConfirm, self.defaultMessages[6])
            return False

        if not re.search(r'[A-Z]', passwrd) or not re.search(r'[a-z]', passwrd) or not re.search(r'\d',passwrd):
            messagebox.showerror("Error", "Password must contain 1 upper case letter, 1 lower case letter, and 1 digit")
            self.resetToDefault(self.userPassword, self.defaultMessages[5])
            self.resetToDefault(self.userPasswordConfirm, self.defaultMessages[6])
            return False
        
        if not self.passwordMatch():
            return False
        
        return True

    def validateDOB(self, dob):
        """
        Validates the user's date of birth.

        Args:
            dob (str): The user's date of birth.

        Returns:
            bool: True if the date of birth has the correct format, False otherwise.
        """
        format = r'^\d{2}-\d{2}-\d{4}$'
        if not re.match(format,dob):
            messagebox.showerror("Error", "Date of birth should have the format dd-mm-yyyy")
            self.resetToDefault(self.userDOB, self.defaultMessages[2])
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
        if widget == self.userPassword or widget == self.userPasswordConfirm:
            widget.bind("<FocusIn>", EntryBoxUtility.handlePasswordFocusIn)
        else:
            widget.bind("<FocusIn>", EntryBoxUtility.handleEntryFocusIn)
        self.focus_set()


    
    
    def validatePhoneNumber(self, phone):
        """
        Validates the user's phone number.

        Args:
            phone (str): The user's phone number.

        Returns:
            bool: True if the phone number has the correct format, False otherwise.
        """
        format = r'^\d{3}-\d{3}-\d{4}'
        if not re.match(format, phone):
            messagebox.showerror("Error", "Phone number should have the format ###-###-####")  
            return False
        return True

    #function that displays success message
    def showSuccessMessage(self, title, message):
        messagebox.showerror(title, message)    
     

    def closeCreate(self):
        self.destroy() 

# Creates instance of App class and starts GUI   
if __name__=="__main__":
    create = Create()
    create.mainloop()           

