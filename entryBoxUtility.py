import tkinter as tk
from tkinter import messagebox
from hashlib import sha3_256

class EntryBoxUtility:
    """
    A utility class for handling entry boxes in tkinter applications.

    Methods:
        clearEntries(event): Clears the entry box when default text is present.
        handlePasswordFocusIn(event): Handles the focus in event for password entry.
        handleEntryFocusOut(event): Handles the focus out event for entry boxes.
    """
    @staticmethod
    def clearEntries(event):
        """
        Clears the entry box when default text is present.

        Args:
            event (tk.Event): The event that triggered the action.
        """
        entryBox = event.widget
        defaultText = entryBox.defaultText
        currentText = entryBox.get()
        if currentText == defaultText:
            entryBox.delete(0, tk.END)

    #@staticmethod
    def handlePasswordFocusIn(event):
        """
        Handles the focus in event for password entry.

        Args:
            event (tk.Event): The event that triggered the action.
        """
        password = event.widget.get()
        if password == event.widget.defaultText:
            event.widget.delete(0, tk.END)  # Clear the entry field if default text is present
        event.widget.config(show="*")   # Show asterisks (*) as user types

    # @staticmethod
    def handleEntryFocusOut(event):
        """
        Handles the focus out event for entry boxes.

        Args:
            event (tk.Event): The event that triggered the action.
        """
        entryInput = event.widget.get()
        if not entryInput:
            event.widget.insert(0, event.widget.defaultText)
            event.widget.config(show="")
    
    # @staticmethod
    def handleEntryFocusIn(event):
        """
        Handles the focus out event for entry boxes.

        Args:
            event (tk.Event): The event that triggered the action.
        """
        entryInout = event.widget.get()
        if entryInout == event.widget.defaultText:
            event.widget.delete(0, tk.END)  
        event.widget.config(show="")   
       
            


       
            
        


   