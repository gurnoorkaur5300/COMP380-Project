import tkinter as tk
from page import Page
from pageHeader import PageHeader

class Login(Page):
     def __init__(self,parent,controller):
        super().__init__(parent,controller)
        
        #add the header
        self.pageHeader = PageHeader(controller)
        self.pageHeader.setPageType("Login")
        
        #create fields
        userEmail = tk.Entry(self, width=35, font =("Arial", 24), bg="white",fg="black")
        userPassword = tk.Entry(self, width=35, font =("Arial", 24), bg="white",fg="black")
        userEmail.insert(0, "Enter username ")
        userPassword.insert(0, "Enter password")

        # Create a new frame to contain the entry widgets
        entryFrame = tk.Frame(self)
        entryFrame.pack()

        # Pack the entry widgets inside the entryFrame
        userEmail.pack(pady=(50, 50))
        userPassword.pack(pady=(50, 50))
        
        #create buttons
        submitButton = tk.Button(self, text = "SUBMIT", borderwidth = 10, font = ("Arial", 32), bg = "white", fg = "black")
        submitButton.pack(padx = 135, side = "left")
        createButton = tk.Button(self, text = "CREATE", borderwidth = 10, font = ("Arial", 32), bg = "white", fg = "black")
        createButton.pack(padx = (0, 135), side = "right",)