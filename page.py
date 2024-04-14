import tkinter as tk

#base class for individual pages
class Page(tk.Frame):
    #function to initialize new instance of class
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
    # switch page/ frame
    # def show(self):
    #     self.lift()
        