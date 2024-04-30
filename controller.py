import tkinter as tk 
from tkinter import ttk 
from database import Database
from page import Page
from navigationBar import NavigationBar
from home import Home
from policies import Policies
from account import Account
from pageHeader import PageHeader
from login import Login
from admin import Admin     
from viewReservation import ViewReservation


#central controller class 
class App(tk.Tk):
    """
    This class represents the central controller of the application.
    :Gregory Calderon
    :version 1.0

    Attributes:
        db (Database): An instance of the Database class.
        isLoggedIn (bool): Flag indicating whether a user is logged in or not. Defaults to False.
        isAdmin (bool): Flag indicating whether the logged-in user is an admin or not. Defaults to False.
        homePage (Home): Instance of the Home page.
        policiesPage (Policies): Instance of the Policies page.
        accountPage (Account): Instance of the Account page.
        adminPage (Admin): Instance of the Admin page.
        loginPage (Login): Instance of the Login page.
        frames (dict): Dictionary containing instances of all pages.

    Methods:
        showFrame(pageName): Displays the specified page.
        showNavbar(): Displays the main navigation bar.
        createFooter(): Creates the footer label for the application.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the App class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        tk.Tk.__init__(self, *args, **kwargs)

        self.db = Database()

        # min and max size of window
        self.minsize(width=800, height=800)
        self.maxsize(width=800, height=800)

        #set theme 
        style=ttk.Style()
        style.theme_use("clam")
        
        # Configure main window to expand and contract proportionally
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)  # Container row
        self.grid_rowconfigure(2, weight=0) # Footer Areaß
        self.grid_columnconfigure(0, weight=1) 
      
        # Create a container frame for pages
        self.container = Page(self,self)
        self.container = tk.Frame(self)  
        self.container.grid(row=1, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Instantiate pages
        self.homePage = Home(self.container, self)
        self.policiesPage = Policies(self.container, self)
        self.loginPage = Login(self.container, self.db, self)
        self.accountPage = Account(self.container, self.db,self, self.loginPage)
        self.adminPage = Admin(self.container, self.db, self)
        self.viewReservation = ViewReservation(self.container, self.db, self)
        
        
        self.frames = {
            "Home": self.homePage,
            "Policies": self.policiesPage,
            "Account": self.accountPage,
            "Admin": self.adminPage,
            "Login": self.loginPage,
            "ViewReservation": self.viewReservation
        }
                    
        self.showFrame("Home")
        self.showNavbar()
        self.createFooter()
        
        self.isLoggedIn = False
        self.isAdmin = False

    #change pages
    def showFrame(self, pageName):
        """
        Displays the specified page.

        Args:
            pageName (str): The name of the page to be displayed.
        """
        if pageName == "Logout":
            pageName = "Home"
            self.isLoggedIn = False
            self.isAdmin = False
            self.accountPage.clearAccountPage()

        # Show specific pages
        if pageName in ["Home","Policies"]:
            self.showNavbar()
        elif pageName ==  "Account" and self.isLoggedIn:
            self.showNavbar()

        # Set the page header for the account page if not logged in
        if pageName == "Account" and not self.isLoggedIn:
            self.pageHeader = PageHeader(self, self)
            pageName = "Login"
            self.pageHeader.setPageType(pageName)

        # Set the page type for the admin page if logged in as an admin
        elif pageName == "Admin" and self.isAdmin and self.isLoggedIn:
            self.pageHeader.setPageType(pageName)

        # Get the page from the frames dictionary
        page = self.frames.get(pageName)
        if page:    
            page.grid(row=0, column=0, sticky="nsew")
            page.tkraise()
        self.update_idletasks()

            
    #display main navbar
    def showNavbar(self):
        """Displays the main navigation bar."""
        self.navbar = NavigationBar(self, self, initialState=False)
        self.navbar.grid(row=0, column=0, sticky="w")
        self.update_idletasks()

    def createFooter(self):
        """Creates the footer label for the application."""
        footer = tk.Label(self, text="© 2024 Titan Reservations, Inc. All rights reserved.", bg="light grey", fg="black")
        footer.grid(row=2, column=0, sticky="ew")  # Ensure it stretches across the bottom
        self.grid_rowconfigure(2, weight=0)  # Make sure the footer doesn't expand


# Creates instance of App class and starts GUI      
if __name__ == "__main__":
    app = App()
    app.title("Titan Reservations")
    app.mainloop()
