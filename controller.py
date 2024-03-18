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
        
        #navbar assigned to top of each page
        self.navbar = NavigationBar(self,self)
        self.navbar.pack(side="top", fill="x")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames = {}
        
        
        #add pages to tuple
        #Login, Create,  Room, View, Cancel, 
        for F in ( Home, Policies, Account):
            pageName = F.__name__
            #for each page we need an instance of that class
            frame = F(container,self)
            #add each page to self.frames dictionary 
            self.frames[pageName] = frame
            frame.grid(row=0,column=0,sticky="nsew")
            
        #by default, display home page
        self.showFrame("Home")
     
    #show frame function   
    def showFrame(self, pageName):
        frame=self.frames[pageName]
        frame.show()

#creates instance of App class and starts GUI      
if __name__ == "__main__":
    app = App()
    app.mainloop()
            