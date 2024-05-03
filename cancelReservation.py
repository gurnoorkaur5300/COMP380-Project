import tkinter as tk
from tkinter import messagebox
from entryBoxUtility import EntryBoxUtility

class CancelReservation(tk.Toplevel):
    def __init__(self,controller, database, master=None):
        """
        Initializes the Create window.
        :author: Arameh Baghdasarian
        :version: 1.0
        Args:
            controller: The controller object responsible for managing page navigation.
            database: The database object containing user information.
            master: The master widget under which this window is placed.
        """
        super().__init__(master)
        self.controller= controller
        self.database = database 
        self.title("Cancel Reservation")
        self.geometry("600x300")


        message_label = tk.Label(self, text="Are you sure you want to cancel the reservation?", font=("Arial", 16))
        message_label.pack(pady=(20, 10)) 

        #create frame for fields
        entryFrame = tk.Frame(self)
        entryFrame.pack()
   

        #create button to submit
        cancelButton = tk.Button(
            self,
            text = "Yes, cancel", 
            borderwidth=10, font=("Arial", 22), 
            bg = "white", fg ="black",  
            activeforeground="blue", 
            command= self.getData)
        cancelButton.pack(padx = 200, side = "left")

        noButton = tk.Button(
            self, 
            text = "No", 
            borderwidth=10, 
            font=("Arial", 22),
            bg = "white", 
            fg ="black",  
            activeforeground="blue", 
            command= self.getData)
        noButton.pack(padx = 200, side = "right")


    #function that displays success message
    def showSuccessMessage(self, title, message):
        messagebox.showerror(title, message)    
     

    def closeCreate(self):
        self.destroy() 

# Creates instance of App class and starts GUI   
if __name__=="__main__":
    cancelReservation = CancelReservation()
    cancelReservation.mainloop()           
