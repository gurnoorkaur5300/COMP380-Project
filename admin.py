import tkinter as tk
from page import Page
from pageHeader import PageHeader

class Admin(Page):
    def __init__(self,parent, controller):
        super().__init__(parent, controller)
        
        #add the header 
        self.pageHeader=PageHeader(controller)
        self.pageHeader.setPageType("Admin")
        
        
        
