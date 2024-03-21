from tkinter import PhotoImage
import tkinter as tk

class NavigationBar(tk.Frame):
    def __init__(self, parent, controller, initialState=False):
        super().__init__(parent)
        self.controller = controller
        
        # Dictionary of colors
        self.color = {"nero": "#252726", "beige": "#F5F5DC", "orange": "#FF8700", "darkorange": "#FE6101"}

        # Setting switch start
        self.btnState = initialState  

        self.navbarBtn = tk.Button(self, text="☰", bg=self.color["nero"], activebackground=self.color["nero"], bd=0, height=3,padx=20, command=self.switch)
        self.navbarBtn.grid(row=0, column=0, sticky="nw")

        # Setting Navbar frame
        self.navRoot = tk.Frame(parent, bg=self.color["nero"], height=400, width=300)

        # Set y coord of navbar widgets
        y = 80
        # Options in navbar
        options = ["Home", "Account", "Policies"]
        
        #for each option in the navbar, when an option is selected, switch tothat page
        for option in options:
            def switchPage(page=option):
                self.switch()
                self.controller.showFrame(page)
                
            tk.Button(self.navRoot, text=option, bg=self.color["nero"], fg=self.color["orange"], activebackground=self.color["orange"], activeforeground="green", bd=0,command=switchPage, width=20, height=2, padx=20, pady=10).place(x=25, y=y)
            y += 80
        
        # Navbar close button
        self.closeBtn = tk.Button(self.navRoot, bg=self.color["orange"], activebackground=self.color["orange"], text="✖", bd=0, command=self.switch)
        self.closeBtn.place(x=250, y=10)
        
        if initialState:
            self.navRoot.grid(row=1, column=0, sticky="nsw")

    def switch(self):
        if self.btnState is True:
            # Close navbar animation
            for x in range(0,301,5):
                self.navRoot.place(x=-x, y=0)
                self.update()

            # Turn button off
            self.btnState = False
        else:
            # Open navbar animation
            for x in range(-301, 0, 5):
                self.navRoot.place(x=x, y=0)
                self.update()
                self.navbarBtn.config(bg=self.color["nero"],activebackground=self.color["nero"])
            self.btnState = True
          
   
