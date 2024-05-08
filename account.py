import tkinter as tk
import tkmacosx
from page import Page
from viewReservation import ViewReservation



class Account(Page):
    """
    This class represents the account page.
    :author: Gregory Calderon
    :version: 3.0

    Attributes:
        parent: The parent widget to which the account page belongs.
        database: The database object containing customer information.
        controller: The controller object responsible for managing page navigation.
        customer: The customer object whose account information is displayed.

    Methods:
        setCustomer(n_customer): Sets the customer whose account information will be displayed.
    """
    def __init__(self,parent, database, controller, loginPage = None, customer=None):
        """
        Initializes the Account object.

        Args:
            parent: The parent widget to which the account page belongs.
            database: The database object containing customer information.
            controller: The controller object responsible for managing page navigation.
            customer: The customer object whose account information is displayed. Default is None.
        """
        super().__init__(parent,controller)
        self.controller = controller
        self.database = database 
        self.customer = customer
        self.loginPage = loginPage

    def clearAccountPage(self):
        """
        Clears the account page by resetting the text of displayed information.
        """
        """
        Logs out the user.
        """
        self.clearLoginEntryBoxes()

    def clearLoginEntryBoxes(self):
        """
        Clears the login entry boxes.
        """     
        if hasattr(self.controller, 'loginPage') and callable(getattr(self.controller.loginPage, 'reset', None)):
            self.controller.loginPage.reset()

    def setCustomer(self, n_customer):
        """
        Sets the customer whose account information will be displayed.

        Args:
            n_customer: The customer object whose account information will be displayed.
        """
        self.customer = n_customer
    
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
         
        infoBox = tk.Frame(self)
        infoBox.grid(row=0,column=0,padx=(35,35), pady=75,sticky="ew")

        labelsInfo = [
        ("Id:", self.customer.id),
        ("Name:", self.customer.name),
        ("Email:", self.customer.email),
        ("Phone:", self.customer.phoneNumber),
        ("DOB:", self.customer.dob)
        ]

        self.infoLabels = []

        for i, (labelText, value) in enumerate(labelsInfo):
            label = tk.Label(infoBox, text=labelText, font=("Arial", 24, "bold"), bg="white", fg="black")
            label.grid(row=i, column=0, padx=15, sticky="e")

            valueLabel = tk.Label(infoBox, text=value, bg="white", fg="black", anchor="w", font=("Ariel",24), width=50)
            valueLabel.grid(row=i, column=1, pady=15, sticky="w")
            self.infoLabels.append(valueLabel)

        self.reservationFrame = tk.Frame(self)
        self.reservationFrame.grid(row=1, column=0, padx=(35,35), sticky="ew")
          
        self.loadReservation()
    
    def clearReserveFrame(self):
        """
        Clears all widgets in the reservation frame.

        This method iterates through all widgets inside the reservation frame and destroys them.

        Args:
            self: The object instance.

        Returns:
            None
        """
        for widget in self.reservationFrame.winfo_children():
            widget.destroy()
       
    def loadReservation(self):
        """
        Loads reservations into the reservation frame.

        This method retrieves reservations from the database for the current customer and displays them as buttons in the reservation frame.
        Each button, when clicked, will call the showReservation method with the corresponding reservation ID.

        Args:
            self: The object instance.

        Returns:
            None
        """
        # print("loading")
        reservationsLabel = tk.Label(self.reservationFrame, text="Reservations:", font=("Arial", 24, "bold"), bg="white", fg="black")
        reservationsLabel.grid(row=0, column=0, sticky="e", padx=15)
        self.customer.reservations.clear()
        self.customer.addReservations(self.database.getReservations(self.customer.id))
        for i, reservation in enumerate(self.customer.reservations):
            reserveId = reservation.split(":")[0].strip()
            
            reservationButton = tk.Button(self.reservationFrame, text=reservation, command=lambda: self.showReservation(reserveId), anchor="center", bg="white", fg="black", font=(18), width=14)
            reservationButton.grid(row= 0, column=i+1, sticky='w', padx=5)
            
        
    def showReservation(self, reserveId):
        """
        Displays details of a reservation.

        This method retrieves information about a reservation from the database based on the provided reservation ID.
        It then sets various attributes of the ViewReservation controller before showing the ViewReservation frame.

        Args:
            self: The object instance.
            reserveId (int): The ID of the reservation to be displayed.

        Returns:
            None
        """
        resInfoTuple = self.database.getResInfo(reserveId)
        self.controller.viewReservation.setCustomerEmail(self.customer.email)
        self.controller.viewReservation.setCustomerName(self.customer.name)
        self.controller.viewReservation.setCustomerId(self.customer.id)
        self.controller.viewReservation.setRoomInfo(*resInfoTuple[0])
        self.controller.isNew = False
        self.controller.viewReservation.updateBtn()
        self.controller.viewReservation.setReserveId(reserveId)
        self.controller.showFrame("ViewReservation")
        
    def reset(self):
        """
        Resets the administrative page.
        """
        self.clearAccountPage()
        if self.controller.isAdmin:
            self.controller.showFrame("Admin")
        elif not self.controller.isAdmin:
            self.controller.showFrame("Home")
       