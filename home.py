import tkinter as tk
from tkinter import ttk, simpledialog, font
from PIL import Image, ImageTk
from tkcalendar import Calendar
from page import Page
from hotels import Hotels
import tkmacosx
import threading

LOCATIONS = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

class CalendarDialog(simpledialog.Dialog):
    """
    Represents a calendar dialog box used for selecting dates.
    :author: Gurnoor Kaur
    :version: 3.0
    
    Methods:
        body(master): Builds the body of the dialog with a calendar widget.
        apply(): Applies the selected date from the calendar.
    """

    def body(self, master):
        """
        Builds the body of the dialog with a calendar widget.

        Args:
            master: The parent widget.

        Returns:
            Calendar object for date selection.
        """
        self.calendar = Calendar(master, selectmode='day')
        self.calendar.pack()
        return self.calendar
  
    def apply(self):
        """
        Applies the selected date from the calendar.
        """
        self.result = self.calendar.selection_get()


class Home(Page):
    """
    Represents the home page of the application where users can search for rooms.
    :author: Gurnoor Kaur
    :version: 3.0

    Methods:
        __init__(parent, controller): Initializes the Home object.
        buildSearchForm(): Constructs the search form with fields for check-in, check-out, and location.
        selectDate(dateType): Opens a CalendarDialog to select dates.
        start_search(): Initiates a new thread for the search to avoid freezing.
        search(): Searches for rooms based on provided dates and location.
        addQuotes(): Adds inspirational quotes to the home page.
    """

    def __init__(self, parent, controller):
        """
        Initializes the Home object.

        Args:
            parent: The parent widget.
            controller: The controller object for managing page navigation.
        """
        super().__init__(parent, controller)
        self.controller = controller

        titleFont = font.Font(family="Helvetica", size=30, weight="bold")
        title = tk.Label(self, text="Share Your Travel Dates, and We'll Handle the Rest!", font=titleFont, fg="#003366", bg="white")
        title.pack(pady=30)

        self.buildSearchForm()
        self.addQuotes()
        self.focus_set()

    def buildSearchForm(self):
        """
        Constructs the search form with fields for check-in, check-out, and location.
        """
        searchFrame = tk.Frame(self, bg='white', borderwidth=2, relief="solid", padx=45, pady=20)
        searchFrame.pack(pady=60, padx=100)

        tk.Label(searchFrame, text="Destination:", bg="white", fg='black', font=("Arial", 16)).pack(pady=10)
        self.locationVar = tk.StringVar()
        locationDropdown = ttk.Combobox(searchFrame, textvariable=self.locationVar, values=LOCATIONS, state="readonly", font=("Arial", 14))
        locationDropdown.pack(pady=10)
        locationDropdown.set("Select Location")

        tk.Label(searchFrame, text="Check-in Date:", bg='white', font=("Arial", 16)).pack(pady=10)
        self.checkinVar = tk.StringVar()
        self.checkinEntry = tk.Entry(searchFrame, textvariable=self.checkinVar, width=20, fg="black", bg= "white", font=("Arial", 14))
        self.checkinEntry.pack(pady=10)
        self.checkinEntry.bind("<Button-1>", lambda event: self.selectDate('checkin'))

        tk.Label(searchFrame, text="Check-out Date:", bg='white', font=("Arial", 16)).pack(pady=10)
        self.checkoutVar = tk.StringVar()
        self.checkoutEntry = tk.Entry(searchFrame, textvariable=self.checkoutVar, width=20, fg="black", bg= "white", font=("Arial", 14))
        self.checkoutEntry.pack(pady=10)
        self.checkoutEntry.bind("<Button-1>", lambda event: self.selectDate('checkout'))

        button = tkmacosx.Button(searchFrame, text="Search Rooms", command=self.search, bg="#003366", fg="white", font=("Arial", 18))
        button.pack(pady=30)

    def selectDate(self, dateType):
        """
        Opens a CalendarDialog to select dates.

        Args:
            dateType: The type of date to select (check-in or check-out).
        """
        dialog = CalendarDialog(self)

        if dialog.result:
            formattedDate = dialog.result.strftime("%Y-%m-%d")
            if dateType == 'checkin':
                self.checkinVar.set(formattedDate)
            elif dateType == 'checkout':
                self.checkoutVar.set(formattedDate)
        self.after(100, self.focus_set)
        dialog.update()

    def start_search(self):
        """
        Initiates a new thread for the search to avoid freezing during API calls.
        """
        search_thread = threading.Thread(target=self.search)
        search_thread.start()

    def search(self):
        """
        Searches for rooms based on provided dates and location.

        This method retrieves the destination ID and uses it to fetch available hotels.
        """
        checkinDate = self.checkinVar.get()
        checkoutDate = self.checkoutVar.get()
        location = self.locationVar.get()

        destination_id = Hotels.get_destination_id(location)
        if not destination_id:
            print("Destination not found.")
            return
        
        hotels_data = Hotels.fetch_hotels(destination_id, checkinDate, checkoutDate)
        print(hotels_data)

    def addQuotes(self):
        """
        Adds inspirational quotes to the home page.
        """
        quotesFrame = tk.Frame(self, bg='white', borderwidth=0)
        quotesFrame.pack(pady=10, fill=tk.X)
        quote = tk.Label(quotesFrame, text="To Travel is to Live!", bg='white', fg="#003366", font=("Georgia", 24, "italic"))
        quote.pack()
