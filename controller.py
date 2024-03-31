import tkinter as tk 
from page import Page
from navigationBar import NavigationBar
from home import Home
from policies import Policies
from account import Account
from pageHeader import PageHeader
from login import Login
# from customer import Customer
from admin import Admin
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
      
        # Create a container frame for pages
        self.container = Page(self,self)
        self.container.grid(row=1, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
      
        # Instantiate pages
        self.homePage = Home(self.container, self)
        self.policiesPage = Policies(self.container, self)
        self.accountPage = Account(self.container, self)
        self.adminPage = Admin(self.container, self)
        self.loginPage = Login(self.container, self)
        
        self.frames = {
            "Home": self.homePage,
            "Policies": self.policiesPage,
            "Account": self.accountPage,
            "Admin": self.adminPage,
            "Login": self.loginPage
        }
                    
        # By default, display home page
        self.showFrame("Home")
        self.showNavbar()

        
        self.isLoggedIn = False
        self.isAdmin = False
    
    #change page frames
    def showFrame(self, pageName):
        
        # Show specific pages
        if pageName in ["Home", "Policies"]:
            self.showNavbar()
        elif pageName == "Account":
            self.pageHeader = PageHeader(self,self)
            if not self.isLoggedIn:
                pageName="Login"
                self.pageHeader.setPageType(pageName)
        elif pageName=="Account" and not self.isAdmin and self.isLoggedIn:               
            self.showNavbar()
            pageName="Account"
        elif pageName == "Admin" and self.isAdmin and self.isLoggedIn:
            pageName="Admin"
            self.pageHeader.setPageType(pageName)
    
        # Get the page from the frames dictionary
        page = self.frames.get(pageName)
        if page:    
            # Grid the page
            page.grid(row=0, column=0, sticky="nsew")
            page.tkraise()
            
    #display main navbar
    def showNavbar(self):
        self.navbar = NavigationBar(self, self, initialState=False)
        self.navbar.grid(row=0, column=0, sticky="w")


# Creates instance of App class and starts GUI      
if __name__ == "__main__":
    app = App()
    app.title("Titan Reservations")
    app.mainloop()
