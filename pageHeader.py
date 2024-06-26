import tkinter as tk

class PageHeader:
    """
    This class represents the header component for pages.
    :author: Gregory Calderon
    :version: 3.0

    Attributes:
        parent: The parent widget to which the header belongs.
        controller: The controller object responsible for managing page navigation.
        color (dict): A dictionary containing color codes.
        mainFrame (tk.Frame): The main frame of the header.
        resetFunctions (list): A list of reset functions for all pages.
        pageIs (str): The current page being displayed.
        pageLabel (tk.Label): The label displaying the current page.
        closeBtn (tk.Button): The close button to return to the home page.

    Methods:
        __init__(parent, controller): Initializes the PageHeader object.
        resetPages(controller): Resets all page values and fields to default values.
        setPageType(pageName): Sets the label for the page header.
    """
    def __init__(self, parent, controller):
        """
        Initializes the PageHeader object.

        Args:
            parent: The parent widget to which the header belongs.
            controller: The controller object responsible for managing page navigation.
        """
        self.parent = parent
        self.controller = controller
        # Dictionary of colors
        self.color = {"nero": "#252726", "beige": "#F5F5DC", "orange": "#FF8700"}
        
        #pages this header will go on 
        pages = [controller.loginPage, controller.adminPage, controller.accountPage, controller.viewReservation]
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
        self.closeBtn = tk.Button(self.mainFrame, text="❌", activeforeground="red", activebackground="light blue", bd=0, command=lambda: self.resetPages(controller), height=3,padx=20, pady=10, border=3)
        self.closeBtn.grid(row=0, column=0, padx=10, pady=(10,10),sticky="nw")
        
        # get all the reset functions
        for page in pages:
            if hasattr(page, "reset") and callable(getattr(page, "reset")):
                self.resetFunctions.append(page.reset)
         
    # collect all the reset fuctions and call them for their respective pages
    def resetPages(self, controller):
        """
        Resets all page values and fields to default values.

        Args:
            controller: The controller object responsible for managing page navigation.
        """ 
        currPage = self.pageIs
        print("currPage is ", currPage)
        resetFunction = getattr(controller, f"{currPage.lower()}Page_", None)
        if resetFunction and callable(resetFunction):
        # for resetFunction in self.resetFunctions:
            resetFunction()
        # self.mainFrame.destroy()
        if currPage == "Login" :
            controller.loginPage.reset()
            controller.showFrame("Home")
        elif currPage == "Account" and self.controller.isAdmin:
            controller.showFrame("Admin")
            controller.accountPage.reset()
        elif currPage == "Admin":
            controller.isLoggedIn = False
            controller.isAdmin = False
            controller.adminPage.reset()
            controller.showFrame("Home")
        elif currPage == "ViewReservation":
            controller.isLoggedIn = True
            controller.isAdmin = True
            controller.adminPage.reset()
            # controller.viewReservation.reset()
            controller.showFrame("Admin")
    
    # set the label for the page header
    def setPageType(self, pageName):
        """
        Sets the label for the page header.

        Args:
            pageName (str): The name of the page.
        """
        self.pageIs= pageName
        self.pageLabel.config(text=self.pageIs)
        