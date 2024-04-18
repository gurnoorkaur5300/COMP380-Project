import tkinter as tk
from tkinter import ttk, simpledialog, font
from PIL import Image, ImageTk
from tkcalendar import Calendar
from page import Page
import tkmacosx
import threading

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
       

        titleFont = font.Font(family="Helvetica", size=30, weight="bold")
        title = tk.Label(self, text="Share Your Travel Dates, and We'll Handle the Rest!", font=titleFont, fg="#003366", bg="white")
        title.pack(pady=30)

        self.buildSearchForm()
        self.addQuotes()
        self.focus_set()
        

    def setupBackground(self):
        self.bgImage = Image.open('assets/bk.jpeg')  
        self.bgPhoto = ImageTk.PhotoImage(self.bgImage)
        bgLabel = tk.Label(self, image=self.bgPhoto)
        bgLabel.place(relwidth=1, relheight=1, x=0, y=0)

    def buildSearchForm(self):
        searchFrame = tk.Frame(self, bg='white', borderwidth=2, relief="solid", padx=45, pady=20)
        searchFrame.pack(pady=60, padx=100)

        tk.Label(searchFrame, text="Destination:", bg="white", fg='black', font=("Arial", 16)).pack(pady=10)
        self.locationVar = tk.StringVar()
        locationDropdown = ttk.Combobox(searchFrame, textvariable=self.locationVar, values=LOCATIONS, state="readonly", font=("Arial", 14))
        locationDropdown.pack(pady=10)
        locationDropdown.set("Select Location")

        tk.Label(searchFrame, text="Check-in Date:", bg='white', font=("Arial", 16)).pack(pady=10)
        self.checkinVar = tk.StringVar()
        self.checkinEntry = tk.Entry(searchFrame, textvariable=self.checkinVar, width=20, fg="black", bg= "white",font=("Arial", 14))
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
        dialog = CalendarDialog(self)
        
        if dialog.result:
            formattedDate = dialog.result.strftime("%Y-%m-%d")
            if dateType == 'checkin':
                self.checkinVar.set(formattedDate)
            elif dateType == 'checkout':
                self.checkoutVar.set(formattedDate)
        self.after(100, self.focus_set)
        dialog.update()


       

    def search(self):
        checkinDate = self.checkinVar.get()
        checkoutDate = self.checkoutVar.get()
        location = self.locationVar.get()
        print(f"Searching for rooms in {location} from {checkinDate} to {checkoutDate}")
       

    def addQuotes(self):
        quotesFrame = tk.Frame(self, bg='white', borderwidth=0)
        quotesFrame.pack(pady=10, fill=tk.X)  # Reduced padding here
        quote2 = tk.Label(quotesFrame, text= "To Travel is to Live!", bg='white', fg="#003366", font=("Georgia", 24, "italic"))
        quote2.pack()