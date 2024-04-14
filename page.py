import tkinter as tk

#base class for individual pages
class Page(tk.Frame):
    """
    Base class for individual pages in a tkinter application.
    :author: Gregory Calderon
    :version: 1

    Attributes:
        controller: The controller responsible for managing page transitions.
    """
    #function to initialize new instance of class
    def __init__(self, parent, controller):
        """
        Initializes a new instance of the Page class.

        Args:
            parent: The parent widget to which this page belongs.
            controller: The controller responsible for managing page transitions.
        """
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        