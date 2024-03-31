import tkinter as tk
from pageHeader import PageHeader

class Create(tk.Toplevel):
    def __init__(self,controller, master=None):
        super().__init__(master)
        self.controller= controller
        self.title("Create Account")
        self.geometry("600x600")

        #create fields
        self.userName = tk.Entry(self,width =30, font=("Arial", 20), bg="white", fg="black")
        self.userLastName = tk.Entry(self, width=30,font = ("Arial",20), bg="white", fg="black")
        self.userDOB = tk.Entry(self, width =30, font=("Arial", 20), bg="white", fg="black")
        self.userEmail = tk.Entry(self, width = 30, font = ("Arial", 20), bg="white", fg="black")
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
        self.userPassword.pack(pady=(20,20))
        self.userPasswordConfirm.pack(pady =(20,20))
   

        #create button to submit
        submitButton = tk.Button(self, text = "SUBMIT", borderwidth=10, font=("Arial", 22), bg = "white", fg ="black", command= self.passwordMatch)
        submitButton.pack(padx = 200, side = "left")

        #bid clearEntries method to the FOCUSIN for all widgest that need to be cleared
        self.userName.bind("<FocusIn>", self.clearEntries)
        self.userLastName.bind("<FocusIn>", self.clearEntries)
        self.userDOB.bind("<FocusIn>",self.clearEntries)
        self.userEmail.bind("<FocusIn>", self.clearEntries)
        self.userPassword.bind("<FocusIn>", self.clearEntries)
        self.userPasswordConfirm.bind("<FocusIn>", self.clearEntries)

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
        if passWord == passWordConfirma:
            self.controller.showFrame("Login") 

# Creates instance of App class and starts GUI   
if __name__=="__main__":
    create = Create()
    create.mainloop()           

