import tkinter as tk
from tkinter import messagebox
import hashlib
import re
from customer import Customer
from database import Database

class Create(tk.Toplevel):
    def __init__(self,controller, database, master=None):
        super().__init__(master)
        self.controller= controller
        self.database = database 
        self.title("Create Account")
        self.geometry("600x600")

        #create fields
        self.userName = tk.Entry(self,width =30, font=("Arial", 20), bg="white", fg="black")
        self.userLastName = tk.Entry(self, width=30,font = ("Arial",20), bg="white", fg="black")
        self.userDOB = tk.Entry(self, width =30, font=("Arial", 20), bg="white", fg="black")
        self.userEmail = tk.Entry(self, width = 30, font = ("Arial", 20), bg="white", fg="black")
        self.userPhone = tk.Entry(self, width = 30, font = ("Arial", 20), bg="white", fg="black")
        self.userPassword = tk.Entry(self,width = 30, font = ("Arial",20), bg="white", fg="black")
        self.userPasswordConfirm = tk.Entry(self, width =30, font =("Arial", 20), bg="white", fg="black")
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
        submitButton = tk.Button(self, text = "SUBMIT", borderwidth=10, font=("Arial", 22), bg = "white", fg ="black", command= self.getData)
        submitButton.pack(padx = 200, side = "left")

        #bid clearEntries method to the FOCUSIN for all widgest that need to be cleared
        self.userName.bind("<FocusIn>", self.clearEntries)
        self.userLastName.bind("<FocusIn>", self.clearEntries)
        self.userDOB.bind("<FocusIn>",self.clearEntries)
        self.userEmail.bind("<FocusIn>", self.clearEntries)
        self.userPhone.bind("<FocusIn>", self.clearEntries)
        # self.userPassword.bind("<FocusIn>", self.handlePasswordFocusIn)
        # self.userPassword.bind("<FocusOut>", self.handlePasswordFocusOut)
        # self.userPasswordConfirm.bind("<FocusIn>", self.handleConfirmPasswordFocusIn)
        # self.userPasswordConfirm.bind("<FocusOut>", self.handleConfirmPasswordFocusOut)

        self.update_idletasks()

    #create function that clears entry boxes when default text is present ONLY
    def clearEntries(self,event):
        entryBox = event.widget
        defaultText = entryBox.defaultText
        currentText = entryBox.get()
        if currentText == defaultText:
            entryBox.delete(0, tk.END)

      #Create function that veryfies if Password and Confirm Password match
    def passwordMatch(self):
        passWord = self.userPassword.get()
        passWordConfirma = self.userPasswordConfirm.get()
        if passWord != passWordConfirma:
            self.showSuccessMessage("Error", "Passwords do not match, Press OK and try again") 
            return False
        return True
            

    def getData(self):
        firstName = self.userName.get()
        lastName = self.userLastName.get()
        dob = self.userDOB.get()
        phone = self.userPhone.get()
        email = self.userEmail.get()
        passwrd = self.userPassword.get()

        if not self.validateName(firstName, lastName):
            return False
        if not self.validateEmail(email):
            return False
        if not self.validatePassword(passwrd):
            return False

        name = firstName + " " + lastName
        hashPasswrd = hashlib.sha256(passwrd.encode()).hexdigest()

        newCustomer = Customer(name, email, dob, phone, hashPasswrd)

        self.database.insertCustomer(newCustomer)

        return True

    def validateName(self, firstN, lastN):
        if not firstN.strip() or not lastN.strip():
            messagebox.showerror("Error", "Please enter both a first and last name")
            return False
        return True

    def validateEmail(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            messagebox.showerror("Error", "Please enter a valid email address")
            return False
        return True

    def validatePassword(self, passwrd):
        if len(passwrd) < 8:
            messagebox.showerror("Error", "Password must be at least 8 characters long")
            return False

        if not re.search(r'[A-Z]', passwrd) or not re.search(r'[a-z]', passwrd) or not re.search(r'\d',passwrd):
            messagebox.showerror("Error", "Password must contain 1 upper case letter, 1 lower case letter, and 1 digit")
            return False
        
        if not self.passwordMatch():
            return False
        
        return True

    
    #function that displays success message
    def showSuccessMessage(self, title, message):
        messagebox.showerror(title, message)    

    #create function to cover password
    def handlePasswordFocusIn(self,event):
        password = self.userPassword.get()
        if password == self.userPassword.defaultText:
            self.userPassword.delete(0, tk.END)
            self.userPassword.config(show="*")

    def handlePasswordFocusOut(self,event):
        password = self.userPassword.get()
        if not password:
            self.userPassword.insert(0, self.userPassword.defaultText)
            self.userPassword.config(show="")

    def handleConfirmPasswordFocusIn(self, event):
        password = self.userPasswordConfirm.get()
        if password == self.userPasswordConfirm.defaultText:
            self.userPasswordConfirm.delete(0, tk.END)
            self.userPasswordConfirm.config(show="*")

    def handleConfirmPasswordFocusOut(self,event):
        password = self.userPasswordConfirm.get()
        if not password:
            self.userPasswordConfirm.insert(0, self.userPasswordConfirm.defaultText)
            self.userPasswordConfirm.config(show="")        

# Creates instance of App class and starts GUI   
if __name__=="__main__":
    create = Create()
    create.mainloop()           

