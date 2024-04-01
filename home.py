import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from page import Page

# Simulated room data (Database to be connected later!)
ROOMS = [
    {
        "name": "Standard Room",
        "image": "assets/standard_room_image.webp",  # Replace with actual image paths
        "amenities": ["1 Bed", "Free WiFi", "TV"],
        "price": "$100/night"
    },
    {
        "name": "Deluxe Room",
        "image": "assets/deluxe_room_image.png",
        "amenities": ["2 Beds", "Free WiFi", "TV", "Ocean View"],
        "price": "$200/night"
    },

]

# Predefined locations for the hotel chain (Assumption : Titans is  a Hotel Chain)
LOCATIONS = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

class Home(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        
        # Title Label
        title = tk.Label(self, text="Welcome to Titan Reservations", font=("Helvetica", 24))
        title.pack(pady=20)
        
        # Building the search form
        self.build_search_form()
        
        # Frame for Room Listings
        self.rooms_frame = tk.Frame(self)
        self.rooms_frame.pack(fill=tk.BOTH, expand=True)
        
    def build_search_form(self):
        search_frame = tk.Frame(self)
        search_frame.pack(pady=10, fill=tk.X)
        
        # Location Dropdown
        tk.Label(search_frame, text="Location:").pack(side=tk.LEFT, padx=5)
        self.location_var = tk.StringVar()
        location_dropdown = ttk.Combobox(search_frame, textvariable=self.location_var, values=LOCATIONS, state="readonly")
        location_dropdown.pack(side=tk.LEFT, padx=5)
        location_dropdown.set("Select Location")  # Default value
        
        # Date Pickers
        tk.Label(search_frame, text="Check-in:").pack(side=tk.LEFT, padx=5)
        self.checkin_date = DateEntry(search_frame)
        self.checkin_date.pack(side=tk.LEFT, padx=5)
        
        tk.Label(search_frame, text="Check-out:").pack(side=tk.LEFT, padx=5)
        self.checkout_date = DateEntry(search_frame)
        self.checkout_date.pack(side=tk.LEFT, padx=5)
        
        # Search Button
        search_btn = tk.Button(search_frame, text="Search", command=self.display_rooms)
        search_btn.pack(side=tk.LEFT, padx=10)
        
    def display_rooms(self):
        location = self.location_var.get()
        checkin = self.checkin_date.get()
        checkout = self.checkout_date.get()
        
        if not location or not checkin or not checkout:
            tk.messagebox.showerror("Error", "Please select location and dates.")
            return
        
        for widget in self.rooms_frame.winfo_children():
            widget.destroy()
        
        for room in ROOMS:
            self.add_room_listing(room)
            
    def add_room_listing(self, room):
        room_frame = tk.Frame(self.rooms_frame, borderwidth=2, relief=tk.GROOVE)
        room_frame.pack(pady=10, padx=10, fill=tk.X)
        
        # Attempt to load and display the room image
        try:
            img = Image.open(room["image"])
            img = img.resize((100, 100), Image.ANTIALIAS)  # Resize to a standard size
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(room_frame, image=img)
            img_label.image = img  # Keep a reference!
            img_label.pack(side=tk.LEFT, padx=5)
        except Exception as e:
            print(f"Error loading image: {e}")
            tk.Label(room_frame, text="Image not found", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)
        
        tk.Label(room_frame, text=room["name"], font=("Helvetica", 16)).pack(side=tk.LEFT, padx=5)
        tk.Label(room_frame, text=f"Price: {room['price']}", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
        
        # Book Room Button
        book_btn = tk.Button(room_frame, text="Book Room", command=lambda: self.book_room(room))
        book_btn.pack(side=tk.RIGHT, padx=10)
        
    def book_room(self, room):
        # Placeholder for booking logic
        print(f"Booking {room['name']}...")
