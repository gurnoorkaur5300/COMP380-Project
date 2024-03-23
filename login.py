import tkinter as tk
from page import Page

class Login(Page):
     def __init__(self,parent,controller):
        super().__init__(parent,controller)
        Page.__init__(self,parent, controller)

        # Dictionary of colors
        self.color = {"nero": "#252726", "beige": "#F5F5DC", "orange": "#FF8700"}

        # Header frame
        self.loginFrame = tk.Frame(controller, bg="beige")
        self.loginFrame.grid(row=0, column=0,sticky="ew")

        for col in range(2):
            self.loginFrame.grid_columnconfigure(col, weight=1)

        # Header label text
        self.loginFrame.grid_columnconfigure(col, weight=1) 
        self.loginLabel = tk.Label(self.loginFrame, text="Titan Hotel Reservations", bg="beige", fg="gray17", height=2, padx=20, pady=5, font=("Ariel",28))
        self.loginLabel.grid(row=0, column=1, sticky="w") 

        self.homeBtn = tk.Button(self.loginFrame, text="☰", bg=self.color["nero"], activebackground=self.color["nero"], bd=0, height=3,padx=20, pady=10)
        self.homeBtn.grid(row=0, column=0, padx=10, pady=(10,10),sticky="nw")

        #create fields
        userEmail = tk.Entry(self, width=35, font =("Arial", 24), bg="white",fg="black")
        userPassword = tk.Entry(self, width=35, font =("Arial", 24), bg="white",fg="black")
        userEmail.insert(0, "Enter username ")
        userPassword.insert(0, "Enter password")

        # Create a new frame to contain the entry widgets
        entryFrame = tk.Frame(self)
        entryFrame.pack()

        # Pack the entry widgets inside the entryFrame
        userEmail.pack(pady=(50, 50))
        userPassword.pack(pady=(50, 50))
        
        #create buttons
        submitButton = tk.Button(self, text = "SUBMIT", borderwidth = 10, font = ("Arial", 32), bg = "white", fg = "black")
        submitButton.pack(padx = 135, side = "left")
        createButton = tk.Button(self, text = "CREATE", borderwidth = 10, font = ("Arial", 32), bg = "white", fg = "black")
        createButton.pack(padx = (0, 135), side = "right",)