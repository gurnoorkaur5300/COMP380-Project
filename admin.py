import tkinter as tk
from tkinter import ttk
from page import Page
import tkmacosx
from tkinter import messagebox
class Admin(Page):
    """
    This class represents the administrative page.
    :author: Gregory Calderon
    :version: 1.0

    Attributes:
        parent: The parent widget to which the administrative page belongs.
        database: The database object containing customer and reservation information.
        controller: The controller object responsible for managing page navigation.

    Methods:
        __init__(parent, database, controller): Initializes the Admin object.
        displayData(): Displays customer and reservation data in the spreadsheet.
        reset(): Resets the administrative page.
    """
    def __init__(self,parent, database, controller):
        """
        Initializes the Admin object.

        Args:
            parent: The parent widget to which the administrative page belongs.
            database: The database object containing customer and reservation information.
            controller: The controller object responsible for managing page navigation.
        """
        super().__init__(parent,controller)
        self.controller = controller
        self.database = database 
        
        #create frame 
        self.spreadsheetFrame=ttk.Frame(self)
        
        #display the frame
        self.spreadsheetFrame.pack(expand=True, fill="both")

        #create spreadsheet object
        self.spreadsheet = ttk.Treeview(self.spreadsheetFrame, columns=("ID", "Name", "ResID", "CheckIn", "CheckOut", "Cost"), show="headings")

        self.spreadsheet.column("#1", width=50)  
        self.spreadsheet.column("#2", width=100)
        self.spreadsheet.column("#3", width=70)
        self.spreadsheet.column("#4", width=75)
        self.spreadsheet.column("#5", width=75)
        self.spreadsheet.column("#6", width=60)
    

        
        #create headings for spreadsheet columns
        self.spreadsheet.heading("#1", text="ID")
        self.spreadsheet.heading("#2", text="Name")
        self.spreadsheet.heading("#3", text="ResID")
        self.spreadsheet.heading("#4", text="CheckIn")
        self.spreadsheet.heading("#5", text="CheckOut")
        self.spreadsheet.heading("#6", text="Cost")

       

        self.update_idletasks()
         
        def displayData():
            """
            Displays customer and reservation data in the spreadsheet.
            """
            #check if data already displayed
            if self.spreadsheet.get_children():
                return
            
            customers = self.database.getCustomerInfo()
            reservations = self.database.getResInfo()
            for customer in customers:
                self.spreadsheet.insert("", "end", values=customer)

            for reservation in reservations:
                self.spreadsheet.insert("", "end", values=reservation)

            self.spreadsheet.bind("<<TreeviewSelect>>", self.on_select)

         #display spreadsheet .pack method 
        self.spreadsheet.pack(expand=True, fill="both")

        # display spreadsheet button
        adminDisplayButton = tkmacosx.Button(self, text="Fetch Data", command=displayData)
        adminDisplayButton.pack()

    def on_select(self, event):
        # Get the selected items
        items = self.spreadsheet.selection()
        if items:  # Check if any item is selected
            item = items[0]  # Get the first selected item
            # Get the values of the selected item
            values = self.spreadsheet.item(item, "values")
            if values:  # Ensure values exist
                customerId = values[0]  
                # write a function in the database
                
                self.showAccountPage(customerId)


    def showAccountPage(self, customerId):
        customer = self.database.getById(customerId)
        if customer:
            self.controller.accountPage.setCustomer(customer)
            self.controller.showFrame("Account")
        else:
            messagebox.showerror("Error", "Customer not found.")


    #reset fuction to be caught by the header close button
    def reset(self):
        """
        Resets the administrative page.
        """
        #clear spreadsheet
        for item in self.spreadsheet.get_children():
            self.spreadsheet.delete(item)
        #reset global variables
        global isLoggedIn, isAdmi
        self.controller.isLoggedIn = False
        self.controller.isAdmin = False
        