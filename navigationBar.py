import tkinter as tk

class NavigationBar(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        #define homeButton variable and style home button
        homeButton = tk.Button(self, text="Home", command=lambda: controller.showFrame("Home"))
        homeButton.grid(row=0,column=0,padx=10,pady=5)
        
        #define accountButton variable and style account button
        accountButton = tk.Button(self, text="Account", command=lambda: controller.showFrame("Account"))
        accountButton.grid(row=0, column=1, padx=10, pady=5)
        
        #define policiesButton variable and style account button
        policiesButton = tk.Button(self, text="Policies", command=lambda: controller.showFrame("Policies"))
        policiesButton.grid(row=0, column=2, padx=10, pady=5)
        
        
    