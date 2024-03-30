import tkinter as tk
from page import Page


class Login(Page):
   def __init__(self,parent,controller):
      super().__init__(parent,controller)
      self.controller = controller

        
      #create fields
      self.userEmail = tk.Entry(self, width=35, font =("Arial", 24), bg="white",fg="black")
      self.userPassword = tk.Entry(self, width=35, font =("Arial", 24), bg="white",fg="black")
      self.userEmail.insert(0, "Enter username ")
      self.userPassword.insert(0, "Enter password")

      # Create a new frame to contain the entry widgets
      entryFrame = tk.Frame(self)
      entryFrame.pack()

      # Pack the entry widgets inside the entryFrame
      self.userEmail.pack(pady=(50, 50))
      self.userPassword.pack(pady=(50, 50))
      
      #dummy submit buttun function to view admin page
      def showUser():
         global isLoggedIn, isAdmin
         self.controller.isLoggedIn = True
         self.controller.isAdmin = True 
         if self.controller.isAdmin:
            self.controller.showFrame("Admin")
         
      #create buttons
      submitButton = tk.Button(self, text = "SUBMIT", borderwidth = 10, font = ("Arial", 32), bg = "white", fg = "black", command=showUser)
      submitButton.pack(padx = 135, side = "left")
      createButton = tk.Button(self, text = "CREATE", borderwidth = 10, font = ("Arial", 32), bg = "white", fg = "black")
      createButton.pack(padx = (0, 135), side = "right",)
        
   #reset function to be caught by page header
   def reset(self):
      self.userEmail.delete(0,tk.END)
      self.userPassword.delete(0,tk.END)
      self.userEmail.insert(0, "Enter username ")
      self.userPassword.insert(0, "Enter password")
      global isLoggedIn, isAdmi
      self.controller.isLoggedIn = False
      self.controller.isAdmin = False
         
   
        