import tkinter as tk

class PageHeader:
    def __init__(self, controller):
    # Dictionary of colors
        self.color = {"nero": "#252726", "beige": "#F5F5DC", "orange": "#FF8700"}

        # main frame
        self.mainFrame = tk.Frame(controller, bg="beige")
        self.mainFrame.grid(row=0, column=0,sticky="ew")

        for col in range(2):
            self.mainFrame.grid_columnconfigure(col, weight=1)
            
        self.pageIs = ""
        
        self.pageLabel = tk.Label(self.mainFrame, text=self.pageIs, bg="beige", fg="gray17", height=2, padx=20, pady=5, font=("Ariel",28))
        self.pageLabel.grid(row=0, column=1, sticky="e") 

        self.closeBtn = tk.Button(self.mainFrame, text="❌", bg=self.color["nero"], activebackground=self.color["nero"], bd=0, command=lambda: controller.showFrame("Home"), height=3,padx=20, pady=10)
        self.closeBtn.grid(row=0, column=0, padx=10, pady=(10,10),sticky="nw")
        
    def setPageType(self, page):
        self.pageIs= page
        self.pageLabel.config(text=self.pageIs)
