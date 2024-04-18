import tkinter as tk
from tkinter import ttk, simpledialog, font
from PIL import Image, ImageTk
from tkcalendar import Calendar
from page import Page

LOCATIONS = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

class CalendarDialog(simpledialog.Dialog):
    def body(self, master):
        self.calendar = Calendar(master, selectmode='day')
        self.calendar.pack()
        return self.calendar

    def apply(self):
        self.result = self.calendar.selection_get()

class Home(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        self.setupBackground()

        titleFont = font.Font(family="Helvetica", size=24, weight="bold")
        title = tk.Label(self, text="Welcome to Titan Reservations", font=titleFont, fg="blue")
        title.pack(pady=20)

        self.buildSearchForm()
        self.addQuotes()

    def setupBackground(self):
        self.bgImage = Image.open('assets/bk.jpeg')  
        self.bgPhoto = ImageTk.PhotoImage(self.bgImage)
        bgLabel = tk.Label(self, image=self.bgPhoto)
        bgLabel.place(relwidth=1, relheight=1, x=0, y=0)

    def buildSearchForm(self):
        searchFrame = tk.Frame(self, bg='white', borderwidth=1, relief="solid")
        searchFrame.pack(pady=30, padx=100)

        tk.Label(searchFrame, text="Destination:", bg='white').pack(pady=5)
        self.locationVar = tk.StringVar()
        locationDropdown = ttk.Combobox(searchFrame, textvariable=self.locationVar, values=LOCATIONS, state="readonly")
        locationDropdown.pack(pady=5)
        locationDropdown.set("Select Location")

        tk.Label(searchFrame, text="Check-in Date:", bg='white').pack(pady=5)
        self.checkinVar = tk.StringVar()
        self.checkinEntry = tk.Entry(searchFrame, textvariable=self.checkinVar, width=15)
        self.checkinEntry.pack(pady=5)
        self.checkinEntry.bind("<Button-1>", lambda event: self.selectDate('checkin'))

        tk.Label(searchFrame, text="Check-out Date:", bg='white').pack(pady=5)
        self.checkoutVar = tk.StringVar()
        self.checkoutEntry = tk.Entry(searchFrame, textvariable=self.checkoutVar, width=15)
        self.checkoutEntry.pack(pady=5)
        self.checkoutEntry.bind("<Button-1>", lambda event: self.selectDate('checkout'))

        tk.Button(searchFrame, text="Search Rooms", command=self.search).pack(pady=20)

    def selectDate(self, dateType):
        dialog = CalendarDialog(self)
        if dialog.result:
            formattedDate = dialog.result.strftime("%Y-%m-%d")
            if dateType == 'checkin':
                self.checkinVar.set(formattedDate)
            elif dateType == 'checkout':
                self.checkoutVar.set(formattedDate)

    def search(self):
        checkinDate = self.checkinVar.get()
        checkoutDate = self.checkoutVar.get()
        location = self.locationVar.get()
        print(f"Searching for rooms in {location} from {checkinDate} to {checkoutDate}")

    def addQuotes(self):
        quotesFrame = tk.Frame(self, bg='white', borderwidth=0)
        quotesFrame.pack(pady=20, fill=tk.X)
        quote1 = tk.Label(quotesFrame, text="“Travel is the only thing you buy that makes you richer.”", bg='white', fg="black")
        quote1.pack()
        quote2 = tk.Label(quotesFrame, text="“To Travel is to Live.” – Hans Christian Andersen", bg='white', fg="black")
        quote2.pack()

