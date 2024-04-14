import tkinter as tk
from tkinter import ttk
from page import Page

class Admin(Page):
    def __init__(self,parent, database, controller):
        super().__init__(parent,controller)
        self.controller = controller
        self.database = database 
        
        #create frame 
        self.spreadsheetFrame=ttk.Frame(self)
        
        #display the frame
        self.spreadsheetFrame.pack(expand=True, fill="both")
         
        def displayData():
            #check if data already displayed
            if self.spreadsheet.get_children():
                return
            
            customers = self.database.getCustomerInfo()
            reservations = self.database.getResInfo()
            for customer in customers:
                self.spreadsheet.insert("", "end", values=customer)

            for reservation in reservations:
                self.spreadsheet.insert("", "end", values=reservation)


            
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

        #display spreadsheet .pack method 
        self.spreadsheet.pack(expand=True, fill="both")
        
        # display spreadsheet button
        adminDisplayButton = tk.Button(self, text="Fetch Data", command=displayData)
        adminDisplayButton.pack()

        self.update_idletasks()
    
    #reset fuction to be caught by the header close button
    def reset(self):
        #clear spreadsheet
        for item in self.spreadsheet.get_children():
            self.spreadsheet.delete(item)
        #reset global variables
        global isLoggedIn, isAdmi
        self.controller.isLoggedIn = False
        self.controller.isAdmin = False
        