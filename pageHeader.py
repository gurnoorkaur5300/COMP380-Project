import tkinter as tk

class PageHeader:
    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        # Dictionary of colors
        self.color = {"nero": "#252726", "beige": "#F5F5DC", "orange": "#FF8700"}
        
        #pages this header will go on 
        pages = [controller.loginPage, controller.adminPage]
        #array of reset fuctions for all pages 
        self.resetFunctions=[]

        # main frame
        self.mainFrame = tk.Frame(parent, bg="beige")
        self.mainFrame.grid(row=0, column=0,sticky="ew")
    
        #make sure frame expands with page
        for col in range(2):
            self.mainFrame.grid_columnconfigure(col, weight=1)

        #initialize header  
        self.pageIs = ""
        
        #page label for header 
        self.pageLabel = tk.Label(self.mainFrame, text="", bg="beige", fg="gray17", height=2, padx=20, pady=5, font=("Ariel",28))
        self.pageLabel.grid(row=0, column=1, sticky="e") 

        #close button on header. should close page and return to home while also clearing all page values and resettig fields to defualt values
        self.closeBtn = tk.Button(self.mainFrame, text="❌", bg=self.color["nero"], activebackground=self.color["nero"], bd=0, command=lambda: self.resetPages(controller), height=3,padx=20, pady=10)
        self.closeBtn.grid(row=0, column=0, padx=10, pady=(10,10),sticky="nw")
        
        # get all the reset functions
        for page in pages:
            if hasattr(page, "reset") and callable(getattr(page, "reset")):
                self.resetFunctions.append(page.reset)
         
    # collect all the reset fuctions and call them for their respective pages
    def resetPages(self, controller): 
        for resetFunction in self.resetFunctions:
            resetFunction()
        controller.showFrame("Home")
    
    # set the label for the page header
    def setPageType(self, pageName):
        print("Setting page type:", pageName)
        self.pageIs= pageName
        self.pageLabel.config(text=self.pageIs)
        
