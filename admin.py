import tkinter as tk
from tkinter import ttk
from page import Page

class Admin(Page):
    def __init__(self,parent, controller):
        super().__init__(parent, controller)
        
        #create frame 
        self.spreadsheetFrame=ttk.Frame(self)
        
        #display the frame
        self.spreadsheetFrame.pack(expand=True, fill="both")
        
        #dummy test data 
        def displayData():
            #dummy list of tuple representing customers to be imported 
            data = [
            (1, "Gregory", "12/5/24"),
            (2, "Martin", "10/2/24"),
            (3, "Gurnoor", "10/22/24"),
            (4, "Arameh", "11/2/24"),
            ]
        
            #insert each row from database into a spreadsheet
            for row in data: 
                self.spreadsheet.insert("", "end", values=row)
            
        #create spreadsheet object
        self.spreadsheet = ttk.Treeview(self.spreadsheetFrame,columns=("ID", "First Name", "Reservation Date"), show="headings")
        
        #create headings for spreadsheet columns
        self.spreadsheet.heading("#1", text="ID")
        self.spreadsheet.heading("#2", text="First Name")
        self.spreadsheet.heading("#3", text="Reservation Date")

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
        