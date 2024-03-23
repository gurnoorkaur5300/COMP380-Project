import tkinter as tk

class Login(tk.Toplevel):
    def __init__(self):
        super().__init__()
        
        self.title("Login")
        
        entryBox = tk.Entry(self, width=50, font=("Arial", 24), bg="white", fg="black")
        
        entryBox.insert(0, "Enter you username")
        
        entryBox.pack(padx=20, pady=(15,20))
        