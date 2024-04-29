import tkinter as tk
from tkinter import ttk, simpledialog, font, messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar
import threading
from page import Page
from hotels import Hotels

LOCATIONS = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

class CalendarDialog(simpledialog.Dialog):
    """
    Represents a calendar dialog box used for selecting dates.
    """
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

        titleFont = font.Font(family="Helvetica", size=30, weight="bold")
        title = tk.Label(self, text="Share Your Travel Dates, and We'll Handle the Rest!", font=titleFont, fg="#003366", bg="white")
        title.pack(pady=30)

        self.buildSearchForm()
        self.addQuotes()
        self.focus_set()

    def buildSearchForm(self):
        searchFrame = tk.Frame(self, bg='white', borderwidth=2, relief="solid", padx=45, pady=20)
        searchFrame.pack(pady=60, padx=100)

        # Destination field
        tk.Label(searchFrame, text="Destination:", bg="white", fg='black', font=("Arial", 16)).pack(pady=10)
        self.locationVar = tk.StringVar()
        locationDropdown = ttk.Combobox(searchFrame, textvariable=self.locationVar, values=LOCATIONS, state="readonly", font=("Arial", 14))
        locationDropdown.pack(pady=10)
        locationDropdown.set("Select Location")

        # Check-in and check-out fields
        tk.Label(searchFrame, text="Check-in Date:", bg='white', font=("Arial", 16)).pack(pady=10)
        self.checkinVar = tk.StringVar()
        self.checkinEntry = tk.Entry(searchFrame, textvariable=self.checkinVar, width=20, fg="black", bg="white", font=("Arial", 14))
        self.checkinEntry.pack(pady=10)
        self.checkinEntry.bind("<Button-1>", lambda event: self.selectDate('checkin'))

        tk.Label(searchFrame, text="Check-out Date:", bg='white', font=("Arial", 16)).pack(pady=10)
        self.checkoutVar = tk.StringVar()
        self.checkoutEntry = tk.Entry(searchFrame, textvariable=self.checkoutVar, width=20, fg="black", bg="white", font=("Arial", 14))
        self.checkoutEntry.pack(pady=10)
        self.checkoutEntry.bind("<Button-1>", lambda event: self.selectDate('checkout'))

        # Search button
        searchButton = tk.Button(searchFrame, text="Search", command=self.start_search, bg="#003366", fg="white", font=("Arial", 18))
        searchButton.pack(pady=30)

    def selectDate(self, dateType):
        dialog = CalendarDialog(self)
        if dialog.result:
            formattedDate = dialog.result.strftime("%Y-%m-%d")
            if dateType == 'checkin':
                self.checkinVar.set(formattedDate)
            elif dateType == 'checkout':
                self.checkoutVar.set(formattedDate)

    def start_search(self):
        search_thread = threading.Thread(target=self.search)
        search_thread.start()

    def search(self):
        checkin_date = self.checkinVar.get()
        checkout_date = self.checkoutVar.get()
        location = self.locationVar.get()
        print(f"Search initiated for location: {location}, Check-in: {checkin_date}, Check-out: {checkout_date}")
    
        hotels_data = Hotels.get_hotels_by_location(location)
        print(f"Hotels found: {hotels_data}")
    
        if not hotels_data:
            tk.messagebox.showinfo("No Hotels", f"No hotels found in {location}.")
            return
    
        self.display_hotels(hotels_data)
    

    def display_hotels(self, hotels):
        hotels_frame = tk.Frame(self, bg='white')
        hotels_frame.pack(pady=20)

        for hotel in hotels:
            hotel_frame = tk.Frame(hotels_frame, borderwidth=2, relief="solid", padx=20, pady=20)
            hotel_frame.pack(pady=10, fill=tk.X)

            # Display hotel image
            image = Image.open(hotel['image_path'])
            image = image.resize((100, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image)
            img_label = tk.Label(hotel_frame, image=img)
            img_label.image = img  # Reference to prevent garbage collection
            img_label.pack(side=tk.LEFT, padx=10)

            # Display hotel information
            hotel_info = f"{hotel['name']} - {hotel['price_range']}\nAmenities: {', '.join(hotel['amenities'])}"
            hotel_label = tk.Label(hotel_frame, text=hotel_info, justify=tk.LEFT)
            hotel_label.pack(side=tk.LEFT, padx=10)

            # "Show Rooms" button
            show_rooms_button = ttk.Button(hotel_frame, text="Show Rooms")
            show_rooms_button.pack(side=tk.RIGHT, padx=10)

    def addQuotes(self):
        quotes_frame = tk.Frame(self, bg='white')
        quotes_frame.pack(pady=10, fill=tk.X)

        quote = tk.Label(quotes_frame, text="To Travel is to Live!", bg='white', fg="#003366", font=("Georgia", 24, "italic"))
        quote.pack()

