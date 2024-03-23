import tkinter as tk 
#from page import Page
from navigationBar import NavigationBar
from home import Home
from policies import Policies
from account import Account
        #import pages 
from login import Login
from customer import Customer
        # from create import Create
        # from room import Room
        # from view import View
        # from cancel import Cancel       

#central controller class 
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.loginPage = None
        
        #minimum window size when app opens
        self.minsize(width=800, height=600)
        
        # Configure main window to expand and contract proportionally
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)  # Container row
        self.grid_columnconfigure(0, weight=1)
        
        
        # Create a container frame for pages
        self.container = tk.Frame(self)
        self.container.grid(row=1, column=0, sticky="nsew")
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Instantiate pages
        self.homePage = Home(self.container, self)
        self.policiesPage = Policies(self.container, self)
        
        # self.loginPage = Login(self.container, self)
     
        self.frames = {}
        
        # By default, display home page
        self.showFrame("Home")
        
        
        #test customer case
        customerInfo = {
            "name": "Greg",
            "email": "gregory.calderon.514@my.csun.edu",
            "dob": "02/06/1987",
            "reservations": ["2jaifj", "33roij", "8a9a98"]
        } 
        
        customer = Customer(**customerInfo)
        self.accountPage = Account(self.container, self, customer)
        
    # Show frame function   
    def showFrame(self, pageName):
        #by defualt, be logged out
        isLoggedIn = True
        
        def showNavbar():
            self.navbar = NavigationBar(self, self, initialState=False)
            self.navbar.grid(row=0, column=0, sticky="w")
            
        def openLoginPage():
            self.loginPage = Login()
            self.loginPage.protocol("WM_DELETE_WINDOW", loginClose)  # Bind close event
            self.loginPage.mainloop()

        def loginClose():
            self.showFrame("Home")     
            if hasattr(self, "loginPage")and self.loginPage:
                self.loginPage.destroy()
        
        if pageName == "Home" or pageName == "Policies":
            showNavbar() 

        if pageName == "Home":
            self.homePage.grid(row=0, column=0, sticky="nsew")
            self.homePage.tkraise()
        elif pageName == "Policies":
            self.policiesPage.grid(row=0, column=0, sticky="nsew")  
            self.policiesPage.tkraise()
        elif pageName == "Account":
            if not isLoggedIn:
                self.homePage.grid(row=0, column=0, sticky="nsew")
                showNavbar()
                self.homePage.tkraise()
                openLoginPage()
                loginClose()
            else:
                
                showNavbar()
                self.accountPage.grid(row=0, column=0, sticky="nsew")  
                self.accountPage.tkraise()
                
        


# Creates instance of App class and starts GUI      
if __name__ == "__main__":
    app = App()
    app.title("Titan Reservations")
    app.mainloop()
