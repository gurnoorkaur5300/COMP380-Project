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
        self.prev_hovered_item = None
        
        #create frame 
        self.spreadsheetFrame=ttk.Frame(self)
        
        #display the frame
        self.spreadsheetFrame.pack(expand=True, fill="both")

        #create spreadsheet object
        self.spreadsheet = ttk.Treeview(self.spreadsheetFrame, columns=("ID", "Name", "ResID", "CheckIn", "CheckOut", "Cost"), show="headings")

        # widths slightly change to fix the formatting - Gurnoor Kaur
        self.spreadsheet.column("#1", width=50)  
        self.spreadsheet.column("#2", width=50)
        self.spreadsheet.column("#3", width=50)
        self.spreadsheet.column("#4", width=50)
        self.spreadsheet.column("#5", width=50)
        self.spreadsheet.column("#6", width=50)
    

        
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

            self.spreadsheet.bind("<Motion>", lambda event: self.onHover)
            self.spreadsheet.bind("<<TreeviewSelect>>", self.onSelect)
            self.spreadsheet.bind("<Leave>", lambda event: self.clearHover())
            self.schedHoverCheck()

         #display spreadsheet .pack method 
        self.spreadsheet.pack(expand=True, fill="both")
       
        # display spreadsheet button
        adminDisplayButton = tkmacosx.Button(self, text="Fetch Data", command=displayData)
        adminDisplayButton.pack()


    def onSelect(self, event):
        
        items = self.spreadsheet.selection()
        if items:  
            item = items[0]  
            values = self.spreadsheet.item(item, "values")
            if values:  
                customerId = values[0]  
                
                self.showAccountPage(customerId)
            self.spreadsheet.selection_set()

    def clearHover(self):
        """
        Clear the hover effect by resetting the background color of all items.
        """
        # Remove the 'hover' tag from all items
        for item in self.spreadsheet.get_children():
            self.spreadsheet.item(item, tags=())




    def schedHoverCheck(self):
        """
        Schedules the onHover method to be   called repeatedly.
        """
        self.onHover()
        self.after(100, self.schedHoverCheck)

    def onHover(self):
        """
        Highlight the row under the mouse cursor.
        """
    # Get the item ID under the mouse cursor
        item = self.spreadsheet.identify_row(self.spreadsheet.winfo_pointery() - self.spreadsheet.winfo_rooty())

        if item:
        # Check if there was a previously hovered item
            if hasattr(self, 'prev_hovered_item') and self.prev_hovered_item != item:
            # Clear the highlight effect of the previously hovered item
                self.clearHover()

        # Highlight the current hovered row
            self.spreadsheet.item(item, tags=('hover',))
            self.spreadsheet.tag_configure('hover', background='lightblue')

        # Remember the current hovered row
            self.prev_hovered_item = item
        else:
        # Clear the highlight if the mouse is not over any item
            self.clearHover()


    
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
     
        
        