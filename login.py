import tkinter as tk
from page import Page
from create import Create
from entryBoxUtility import EntryBoxUtility
from tkinter import messagebox
import hashlib

class Login(Page):
   """
    This class represents the login page.
    :author: Gregory Calderon and Martin Gallegos Cordero

    Attributes:
        parent: The parent widget to which the login page belongs.
        database: The database object containing user information.
        controller: The controller object responsible for managing page navigation.

    Methods:
        showCreate(): Opens the create user page.
        validateUserLogin(): Validates the user's login credentials.
        showUser(user): Displays the appropriate user interface based on the user's role.
        reset(): Resets the login form fields and state.
    """
   def __init__(self,parent, database, controller):
      """
        Initializes the Login object.

        Args:
            parent: The parent widget to which the login page belongs.
            database: The database object containing user information.
            controller: The controller object responsible for managing page navigation.
        """
      super().__init__(parent,controller)
      self.controller = controller
      self.database = database 

      #create fields
      self.userEmail = tk.Entry(self, width=35, font =("Arial", 24), bg="white",fg="black", insertbackground="black", insertwidth=4)
      self.userPassword = tk.Entry(self, width=35, font =("Arial", 24), bg="white",fg="black", insertbackground="black", insertwidth=4)
      
      #Creating the pre-defined text for entry boxes
      self.userEmail.insert(0, "Enter username")
      self.userEmail.defaultText = "Enter username"
      self.userPassword.insert(0, "Enter password")
      self.userPassword.defaultText = "Enter password"
      
      #Bind the entry boxes
      self.userEmail.bind("<FocusIn>", EntryBoxUtility.clearEntries)
      self.userPassword.bind("<FocusIn>", EntryBoxUtility.clearEntries)
      self.userPassword.bind("<FocusIn>", EntryBoxUtility.handlePasswordFocusIn)
      self.userPassword.bind("<FocusOut>", EntryBoxUtility.handleEntryFocusOut)
      self.userEmail.bind("<FocusOut>", EntryBoxUtility.handleEntryFocusOut)

      # Create a new frame to contain the entry widgets
      entryFrame = tk.Frame(self)
      
      #check box frame 
      checkBoxFrame = tk.Frame(self)
      
      #only let one checkbox be checked at one time 
      def checkBox():
         """
         restricts one check box to being marked at a time
         """
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
         """
         Opens the create user page.
         """
         if self.isUserVar.get() == 1:
           Create(self, database)
         else:
            messagebox.showerror("ERROR", "Unathorized Action")
      
      #arrays to help clear entry boxes
      self.defaultMessages=["Enter username","Enter password"]
      widgets = [self.userEmail, self.userPassword]

      def validateUserLogin(self):
         """
        Validates the user's login credentials.
        """

         email = self.userEmail.get().lower()
         # print(email)
         passWord = self.userPassword.get()
         # print(passWord)
         hashPasswrd = hashlib.sha256(passWord.encode()).hexdigest()
         # print(hashPasswrd)

         
         if database.isVerified(email, hashPasswrd, self.isUserVar.get()):
            if self.isUserVar.get() ==1:
               self.isAdmin=False
               self.isUser=True
               isCustomer = database.getEmail(email)
               showUser(isCustomer)
            else:
               self.isUser=False
               self.isAdmin=True
               isAdmin = database.getAdminEmail(email)
               showUser(isAdmin)
         else:
            self.isUser=False
            messagebox.showerror("Error", "Incorrect Password or Email")
            self.reset(self.userEmail, self.defaultMessages[0])
            self.reset(self.userPassword, self.defaultMessages[1])
            
            

      def showUser(user):
         """
        Displays the appropriate user interface based on the user's role.
        """
         if self.isUser:
            self.controller.isLoggedIn = True
            self.controller.isAdmin = False
            self.controller.accountPage.setCustomer(user)
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
   def reset(self, widget, defaultMessage):
      """
      Resets the login form fields and state.
      """
      global isLoggedIn, isAdmin
      self.controller.isLoggedIn = False
      self.controller.isAdmin = False
      self.isUser = False
      self.isAdmin = False

      widget.delete(0, tk.END)
      widget.insert(0, defaultMessage)
      widget.config(show="")  
      widget.bind("<FocusIn>", EntryBoxUtility.clearEntries)
      if widget == self.userPassword:
         widget.bind("<FocusIn>", EntryBoxUtility.handlePasswordFocusIn)
      else:
         widget.bind("<FocusIn>", EntryBoxUtility.handleEntryFocusIn)
      self.focus_set()
         
   
   # def resetTxt(self):
   #    self.clearEntries()
