import tkinter as tk
from tkinter import ttk, simpledialog, font
from tkcalendar import Calendar
from page import Page

LOCATIONS = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

# Calendar dialog that lets users pick a date.
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
        
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title = tk.Label(self, text="Welcome to Titan Reservations", font=title_font, fg="blue")
        title.pack(pady=20)
        
        self.build_search_form()

    def build_search_form(self):
        search_frame = tk.Frame(self)
        search_frame.pack(pady=10, fill=tk.X)

        tk.Label(search_frame, text="Location:").pack(side=tk.LEFT, padx=5)
        self.location_var = tk.StringVar()
        location_dropdown = ttk.Combobox(search_frame, textvariable=self.location_var, values=LOCATIONS, state="readonly")
        location_dropdown.pack(side=tk.LEFT, padx=5)
        location_dropdown.set("Select Location")

        tk.Label(search_frame, text="Check-in:").pack(side=tk.LEFT, padx=5)
        self.checkin_var = tk.StringVar()
        self.checkin_entry = tk.Entry(search_frame, textvariable=self.checkin_var, width=15)
        self.checkin_entry.pack(side=tk.LEFT, padx=5)
        self.checkin_entry.bind("<Button-1>", lambda event: self.select_date('checkin'))

        tk.Label(search_frame, text="Check-out:").pack(side=tk.LEFT, padx=5)
        self.checkout_var = tk.StringVar()
        self.checkout_entry = tk.Entry(search_frame, textvariable=self.checkout_var, width=15)
        self.checkout_entry.pack(side=tk.LEFT, padx=5)
        self.checkout_entry.bind("<Button-1>", lambda event: self.select_date('checkout'))

        tk.Button(search_frame, text="Search", command=self.search).pack(side=tk.LEFT, padx=10)

    def select_date(self, date_type):
        dialog = CalendarDialog(self)
        if dialog.result:
            formatted_date = dialog.result.strftime("%Y-%m-%d")
            if date_type == 'checkin':
                self.checkin_var.set(formatted_date)
            elif date_type == 'checkout':
                self.checkout_var.set(formatted_date)

    def search(self):
        # To be done - API integration.
        checkin_date = self.checkin_var.get()
        checkout_date = self.checkout_var.get()
        location = self.location_var.get()
        print(f"Searching for rooms in {location} from {checkin_date} to {checkout_date}")

