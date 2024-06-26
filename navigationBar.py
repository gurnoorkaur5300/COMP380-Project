from tkinter import *
import tkinter as tk
import tkmacosx


class NavigationBar(tk.Frame):
    """
    This class represents the navigation bar component.
    :author: Gregory Calderon
    :version: 3.0
    
    Attributes:
        parent: The parent widget to which the navigation bar belongs.
        controller: The controller object responsible for managing page navigation.
        color (dict): A dictionary containing color codes.
        headerFrame (tk.Frame): The frame containing the header.
        homeLabel (tk.Label): The label displaying the home page text.
        btnState (bool): The state of the navigation bar button.
        navbarBtn (tkmacosx.Button): The main navigation bar button.
        navRoot (tk.Frame): The frame for the navigation bar options.
        closeBtn (tkmacosx.Button): The close button for the navigation bar.

    Methods:
        __init__(parent, controller, initialState=False): Initializes the NavigationBar object.
        switch(): Toggles the state of the navigation bar.
    """
    def __init__(self, parent, controller, initialState=False):
        """
        Initializes the NavigationBar object.

        Args:
            parent: The parent widget to which the navigation bar belongs.
            controller: The controller object responsible for managing page navigation.
            initialState (bool): The initial state of the navigation bar. Defaults to False.
        """
        super().__init__(parent)
        self.controller = controller
        
        # Dictionary of colors
        self.color = {"nero": "#252726", "beige": "#F5F5DC"}
        
        # Header frame
        self.headerFrame = tk.Frame(parent, bg="beige")
        self.headerFrame.grid(row=0, column=0,sticky="ew")
        
        for col in range(2):
            self.headerFrame.grid_columnconfigure(col, weight=1) 
        
        # Header label text
        self.homeLabel = tk.Label(self.headerFrame, text="Titan Hotel Reservations", bg="beige", fg=self.color["nero"], height=2, padx= 20, pady=5, font=("Ariel",28))
        self.homeLabel.grid(row=0, column=1, sticky="e")
        
        # Setting switch start
        self.btnState = initialState  

        #main navigation bar button. when clicked will call switch() which animates the bar open and closed
        self.navbarBtn = tkmacosx.Button(self.headerFrame, text="☰", activeforeground="blue", bd=0, height=70, width= 75, padx=20, pady=10, command=self.switch, font=("Helvetica", 40))
        self.navbarBtn.grid(row=0, column=0, padx=10, pady=(10,10), sticky="nw")

        # Setting Navbar frame
        self.navRoot = tk.Frame(parent, bg="beige", height=400, width=300)

        # Set y coord of navbar widgets
        y = 80
        # Options in navbar
        options = ["Home", "Account", "Policies", "Logout"]
        
        #for each option in the navbar, when an option is selected, switch to that page
        for option in options:
            def switchPage(page=option):
                self.switch()
                self.headerFrame.grid_remove()
                self.controller.showFrame(page)
                
            #each item in navbar menu is a button. when the button in the navbar is clicked, that page should be populated using the function switchPage()
            tkmacosx.Button(self.navRoot, text=option, fg=self.color["nero"], activeforeground="blue", bd=0,command= switchPage, width=200, height=40,font=("Helvetica", 20)).place(x=50, y=y)
            y += 80
                
        # Navbar close button
        self.closeBtn = tkmacosx.Button(self.navRoot, text="✖", bd=0, command=self.switch, fg=self.color["nero"],font=("Helvetica", 14), padx=-20)
        self.closeBtn.place(x=230, y=10)
        

        if initialState:
            self.navRoot.grid(row=1, column=0, sticky="nsw")

    def switch(self):
        """
        Toggles the state of the navigation bar.
        """
        if self.btnState is True:
            # Close navbar animation
            for x in range(0,301,5):
                self.navRoot.place(x=-x, y=0)
                self.update_idletasks()

            # Turn button off
            self.btnState = False
        else:
            # Open navbar animation
            for x in range(-301, 0, 5):
                self.navRoot.place(x=x, y=0)
                self.update_idletasks()
            self.btnState = True
          
   