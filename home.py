import tkinter as tk
from tkinter import ttk, simpledialog, font, messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar
import threading
from page import Page
from hotels import Hotels
from database import Database  # Assume Database class handles all database interactions


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
        self.db = Database()  # Initialize the database
        self.scrollable_frame = controller
        # self.hotelsView = HotelsView(self, self.db, self.controller)

        titleFont = font.Font(family="Helvetica", size=30, weight="bold")
        title = tk.Label(self, text="Share Your Travel Dates, and We'll Handle the Rest!", font=titleFont, fg="#003366", bg="white")
        title.pack(pady=30, padx=20, fill=tk.X)

        self.buildSearchForm()
        self.addQuotes()
        self.focus_set()

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
        self.checkinEntry = tk.Entry(searchFrame, textvariable=self.checkinVar, width=20, fg="black", bg="white", font=("Arial", 14))
        self.checkinEntry.pack(pady=10)
        self.checkinEntry.bind("<Button-1>", lambda event: self.selectDate('checkin'))

        tk.Label(searchFrame, text="Check-out Date:", bg='white', font=("Arial", 16)).pack(pady=10)
        self.checkoutVar = tk.StringVar()
        self.checkoutEntry = tk.Entry(searchFrame, textvariable=self.checkoutVar, width=20, fg="black", bg="white", font=("Arial", 14))
        self.checkoutEntry.pack(pady=10)
        self.checkoutEntry.bind("<Button-1>", lambda event: self.selectDate('checkout'))

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
        location = self.locationVar.get()
        checkin_date = self.checkinVar.get()
        checkout_date = self.checkoutVar.get()
        hotels_data = self.db.fetchHotelsByLocation(location)
        if not hotels_data:
            tk.messagebox.showinfo("No Hotels", f"No hotels found in {location}.")
            return
       
        self.controller.hotelsView.setHotelsData(hotels_data, checkin_date, checkout_date)
        self.controller.hotelsView.displayHotels()
        self.controller.showFrame("HotelsView")
        
    def addQuotes(self):
        quotesFrame = tk.Frame(self, bg='white')
        quotesFrame.pack(pady=(10,0), fill=tk.X)
        quote = tk.Label(quotesFrame, text="To Travel is to Live!", bg='white', fg="#003366", font=("Georgia", 24, "italic"))
        quote.pack(padx=10, pady=5)
       

    # def display_hotels(self, hotels, checkin, checkout):
    #     hotels_frame = tk.Frame(self, bg='white')
    #     hotels_frame.pack(pady=20)

    #     for hotel in hotels:
    #         hotel_frame = tk.Frame(hotels_frame, borderwidth=2, relief="solid", padx=20, pady=20)
    #         hotel_frame.pack(pady=10, fill=tk.X)
            
    #         # print(hotel)
    #         photoPath = hotel['photoLink']
    #         try:
    #             image = Image.open(photoPath)
    #             image = image.resize((100, 100))
    #             img = ImageTk.PhotoImage(image)
    #             img_label = tk.Label(hotel_frame, image=img)
    #             img_label.image = img
    #             img_label.pack(side=tk.LEFT, padx=10)
    #         except Exception as e:
    #             print("Error opening or resizing image:", e)
            

    #         hotel_info = f"{hotel['name']} - {hotel['price_range']}\nAmenities: {', '.join(hotel['amenities'])}"
    #         hotel_label = tk.Label(hotel_frame, text=hotel_info, justify=tk.LEFT)
    #         hotel_label.pack(side=tk.LEFT, padx=10)

    #         show_rooms_button = ttk.Button(hotel_frame, text="Show Rooms", command=lambda h=hotel['name']: self.show_rooms(h, checkin, checkout))
    #         show_rooms_button.pack(side=tk.RIGHT, padx=10)

    # def show_rooms(self, hotel_name, checkin, checkout):
    #     rooms = self.db.fetch_rooms_by_hotel_and_availability(hotel_name, checkin, checkout)
    #     for room in rooms:
    #         print(room)
    #     if not rooms:
    #         messagebox.showinfo("Rooms", "No available rooms for the selected dates.")
    #         return
    #     messagebox.showinfo("Rooms", f"Available rooms for {hotel_name}:\n" + '\n'.join([f"Room {room['roomNum']} at ${room['cost']}" for room in rooms]))

  

