import tkinter as tk 
from page import Page
from navigationBar import NavigationBar
from home import Home
from policies import Policies
from account import Account
        #import pages 
        # from login import Login
        # from create import Create
        # from room import Room
        # from view import View
        # from cancel import Cancel

        

#central controller class 
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #minimum window size when app opens
        self.minsize(width=800, height=600)
        
        # Configure main window to expand and contract proportionally
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)  # Container row
        self.grid_columnconfigure(0, weight=1)
        
          
        # Header frame
        self.headerFrame = tk.Frame(self, bg="beige")
        self.headerFrame.grid(row=0, column=0, sticky="ew")  
        self.headerFrame.grid_columnconfigure(0, weight=1)  # Ensure the column expands to fill the space
        self.headerFrame.grid_columnconfigure(1, weight=0)  # Ensure the column with the label doesn't expand
        
        # # Header label text
        self.homeLabel = tk.Label(self.headerFrame, text="Titan Hotel Reservations", bg="beige", fg="gray17", height=2, padx=20, pady=5, font=("Ariel",28))
        self.homeLabel.grid(row=0, column=1, sticky="e")
          
        # Create a container frame for pages
        self.container = tk.Frame(self)
        self.container.grid(row=1, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Instantiate pages
        self.homePage = Home(self.container, self)
        self.policiesPage = Policies(self.container, self)
        self.accountPage = Account(self.container, self)
     
        self.frames = {}
        
        # By default, display home page
        self.showFrame("Home")
     
    # Show frame function   
    def showFrame(self, pageName):
        def showNavbar():
            self.navbar = NavigationBar(self, self, initialState=False)
            self.navbar.grid(row=0, column=0, sticky="w", padx=20) 
        if pageName == "Home" or pageName == "Policies" or pageName == "Account":
            showNavbar() 
           
        if pageName == "Home":
            self.homePage.grid(row=0, column=0, sticky="nsew")
            self.homePage.tkraise()
        elif pageName == "Policies":
            self.policiesPage.grid(row=0, column=0, sticky="nsew")  
            self.policiesPage.tkraise()
        elif pageName == "Account":
            self.accountPage.grid(row=0, column=0, sticky="nsew")  
            self.accountPage.tkraise()


# Creates instance of App class and starts GUI      
if __name__ == "__main__":
    app = App()
    app.title("Titan Reservations")
    app.mainloop()
