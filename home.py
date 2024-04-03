import tkinter as tk
from tkinter import ttk, simpledialog, font
from tkcalendar import Calendar
from PIL import Image, ImageTk
import threading
from page import Page

# mock database of rooms and locations.
ROOMS = [
    {"name": "Standard Room", "image": "assets/standard_room_image.webp", "amenities": ["1 Bed", "Free WiFi", "TV"], "price": "$100/night"},
    {"name": "Deluxe Room", "image": "assets/deluxe_room_image.png", "amenities": ["2 Beds", "Free WiFi", "TV", "Ocean View"], "price": "$200/night"},
]
LOCATIONS = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

# A simple calendar dialog that lets users pick a date.
class CalendarDialog(simpledialog.Dialog):
    def body(self, master):
        self.calendar = Calendar(master)
        self.calendar.pack()
        return self.calendar

    def apply(self):
        self.result = self.calendar.selection_get()

class Home(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.controller = controller
        self.images = {}  # A cache for our room images to speed up loading.
        
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title = tk.Label(self, text="Welcome to Titan Reservations", font=title_font, fg="blue")
        title.pack(pady=20)
        
        # Setting up the form where users will input their booking details.
        self.build_search_form()
        
        # Where we'll display the rooms available.
        self.rooms_frame = tk.Frame(self)
        self.rooms_frame.pack(fill=tk.BOTH, expand=True)
        
        # Kick off image loading in the background to keep the UI snappy.
        self.preload_images_async()

        # Labels for showing the selected check-in and check-out dates.
        self.checkin_var = tk.StringVar(value="Check-in Date: None")
        self.checkout_var = tk.StringVar(value="Check-out Date: None")
        tk.Label(self, textvariable=self.checkin_var, font=("Helvetica", 12), fg="green").pack(pady=2)
        tk.Label(self, textvariable=self.checkout_var, font=("Helvetica", 12), fg="green").pack(pady=2)

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", font=("Helvetica", 12), padding=5)
        style.configure("TLabel", font=("Helvetica", 14), background="lightblue")
        style.configure("TCombobox", font=("Helvetica", 12), padding=5)

    def preload_images_async(self):
        thread = threading.Thread(target=self.preload_images, daemon=True)
        thread.start()

    def preload_images(self):
        for room in ROOMS:
            path = room["image"]
            try:
                # Resize for consistency and to reduce memory usage.
                img = Image.open(path).resize((100, 100), Image.ANTIALIAS)
                self.images[room["name"]] = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Error preloading image {path}: {e}")

    def build_search_form(self):
        # A form for the user to input their booking details.
        search_frame = tk.Frame(self)
        search_frame.pack(pady=10, fill=tk.X)

        # selecting a location.
        tk.Label(search_frame, text="Location:").pack(side=tk.LEFT, padx=5)
        self.location_var = tk.StringVar()
        location_dropdown = ttk.Combobox(search_frame, textvariable=self.location_var, values=LOCATIONS, state="readonly")
        location_dropdown.pack(side=tk.LEFT, padx=5)
        location_dropdown.set("Select Location")

        # selecting check-in and check-out dates.
        tk.Label(search_frame, text="Check-in:").pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Select Date", command=lambda: self.select_date('checkin')).pack(side=tk.LEFT, padx=5)

        tk.Label(search_frame, text="Check-out:").pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Select Date", command=lambda: self.select_date('checkout')).pack(side=tk.LEFT, padx=5)

        # search to find available rooms based on the criteria.
        tk.Button(search_frame, text="Search", command=self.display_rooms).pack(side=tk.LEFT, padx=10)

    def select_date(self, date_type):
        dialog = CalendarDialog(self)
        if dialog.result:
            formatted_date = dialog.result
            if date_type == 'checkin':
                self.checkin_var.set(f"Check-in Date: {formatted_date}")
            elif date_type == 'checkout':
                self.checkout_var.set(f"Check-out Date: {formatted_date}")

    def display_rooms(self):
        for widget in self.rooms_frame.winfo_children():
            widget.destroy()
        for room in ROOMS:
            self.add_room_listing(room)

    def add_room_listing(self, room):
        # For each room, creates a display widget showing its details.
        room_frame = tk.Frame(self.rooms_frame, borderwidth=2, relief=tk.GROOVE)
        room_frame.pack(pady=10, padx=10, fill=tk.X)

        # Retrieves the preloaded image if available.
        image = self.images.get(room["name"], None)
        if image:
            img_label = tk.Label(room_frame, image=image)
            img_label.pack(side=tk.LEFT, padx=5)
        else:
            tk.Label(room_frame, text="Image not found", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)

        tk.Label(room_frame, text=room["name"], font=("Helvetica", 16)).pack(side=tk.LEFT, padx=5)
        tk.Label(room_frame, text=f"Price: {room['price']}", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)

        tk.Button(room_frame, text="Book Room", command=lambda room=room: self.book_room(room)).pack(side=tk.RIGHT, padx=10)

    def book_room(self, room):
        # Placeholder for booking function (console)
        print(f"Booking {room['name']}...")
