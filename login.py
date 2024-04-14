import tkinter as tk
from page import Page
from create import Create
from tkinter import messagebox
import hashlib

class Login(Page):
   def __init__(self,parent, database, controller):
      super().__init__(parent,controller)
      self.controller = controller
      self.database = database 

      #create fields
      self.userEmail = tk.Entry(self, width=35, font =("Arial", 24), bg="white",fg="black", insertbackground="black", insertwidth=4)

      self.userPassword = tk.Entry(self, width=35, font =("Arial", 24), bg="white",fg="black", insertbackground="black", insertwidth=4)
      self.userEmail.insert(0, "Enter username")
      self.userEmail.defaultText = "Enter username"

      self.userPassword.insert(0, "Enter password")
      self.userPassword.defaultText = "Enter password"

      self.userEmail.bind("<FocusIn>", self.clearEntries)
      self.userPassword.bind("<FocusIn>", self.clearEntries)
      self.userPassword.bind("<FocusIn>", self.handlePasswordFocusIn)
      self.userPassword.bind("<FocusOut>", self.handlePasswordFocusOut)

      self.userEmail.bind("<FocusOut>", self.handleUserEmailFocusOut)


      # Create a new frame to contain the entry widgets
      entryFrame = tk.Frame(self)
      
      #check box frame 
      checkBoxFrame = tk.Frame(self)
      
      #only let one checkbox be checked at one time 
      def checkBox():
         global isUser
         if self.isAdminVar.get() == 1:
            self.isUserVar.set(0)
            self.isUserCheck.deselect()
         # If User checkbox is checked, deselect Admin checkbox
         elif self.isUserVar.get() == 1:
            self.isAdminVar.set(0)
            self.isAdminCheck.deselect()
            self.isUser = True
         if self.isUserVar.get() == 0:
            self.isUser = False

      self.isUser=True

      #check box attributes 

      self.isAdminVar = tk.IntVar()
      self.isUserVar = tk.IntVar(value =1)
      self.isAdminCheck = tk.Checkbutton(checkBoxFrame, text="Admin",variable=self.isAdminVar, command=checkBox)
      self.isUserCheck = tk.Checkbutton(checkBoxFrame, text="User", variable=self.isUserVar, command=checkBox)
      self.isAdminCheck.grid(row=0, column=0)
      self.isUserCheck.grid(row=0, column=1)

      # Pack the entry widgets inside the entryFrame
      self.userEmail.pack(side=tk.TOP, pady=(50, 10))
      self.userPassword.pack(side=tk.TOP, pady=(10, 50))

      def showCreate(self):
        Create(self, database) 

      def validateUserLogin(self):
         email = self.userEmail.get()
         # print(email)
         passWord = self.userPassword.get()
         # print(passWord)
         hashPasswrd = hashlib.sha256(passWord.encode()).hexdigest()
         # print(hashPasswrd)
         
         if database.isVerified(email, hashPasswrd):
            showUser()
         else:
            # Assuming you want to bind the clearEntries function to the userEmail and userPassword entry fields
            self.resetTxt()

            messagebox.showerror("Error", "Incorrect Password")
            

      #dummy submit buttun function to view admin page
      def showUser():
         if self.isUser:
            self.controller.isLoggedIn = True
            self.controller.isAdmin = False
            self.controller.showFrame("Account")
         elif not self.isUser:
            self.controller.isLoggedIn = True
            self.controller.isAdmin = True
            self.controller.showFrame("Admin")
            
      #buttons frame
      buttonsFrame = tk.Frame(self)
     
      #create buttons
      submitButton = tk.Button(buttonsFrame, text = "SUBMIT", borderwidth = 10, font = ("Arial", 32), bg = "white", activeforeground="blue", command= lambda: validateUserLogin(self))
      submitButton.pack(side=tk.LEFT, padx = 135)

      createButton = tk.Button(buttonsFrame, text = "CREATE", borderwidth = 10, font = ("Arial", 32), bg = "white", fg = "black", activeforeground="blue", command = lambda:showCreate(self))
      createButton.pack(side=tk.RIGHT, padx = (0, 135))

      #display frames on page 
      entryFrame.pack()
      checkBoxFrame.pack()
      buttonsFrame.pack()

      self.update_idletasks()
        
   #reset function to be caught by page header
   def reset(self):
      self.userEmail.delete(0,tk.END)
      self.userPassword.delete(0,tk.END)
      self.userEmail.insert(0, "Enter username ")

      self.userPassword.insert(0, "Enter password")
      global isLoggedIn, isAdmin
      self.controller.isLoggedIn = False
      self.controller.isAdmin = False
         
   
      #create function that clears entry boxes when default text is present ONLY
   def clearEntries(self,event):
        entryBox = event.widget
        defaultText = entryBox.defaultText
        currentText = entryBox.get()
        if currentText == defaultText:
            entryBox.delete(0, tk.END)

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

   def handleUserEmailFocusOut(self,event):
      email = self.userEmail.get()
      if not email:
         self.userEmail.insert(0, self.userEmail.defaultText)
         self.userEmail.config(show="")

   def resetTxt(self):
      self.clearEntries()
