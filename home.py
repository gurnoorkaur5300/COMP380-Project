import tkinter as tk
from tkinter import ttk, simpledialog, font
from tkcalendar import Calendar
from PIL import Image, ImageTk
import threading
from page import Page
import time
from functools import wraps
import tkmacosx

# Global variables for mock database
ROOMS = [
    {"name": "Standard Room", "image": "assets/standard_room_image.webp", "amenities": ["1 Bed", "Free WiFi", "TV"], "price": "$100/night"},
    {"name": "Deluxe Room", "image": "assets/deluxe_room_image.png", "amenities": ["2 Beds", "Free WiFi", "TV", "Ocean View"], "price": "$200/night"},
]
LOCATIONS = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]


#Debounce decorator to prevent rapid clicks
def debounce(wait):
    """Prevent a function from being called more than once every wait seconds"""
    def decorator(fn):
        @wraps(fn)
        def debounced(*args, **kwargs):
            current_time = time.time()
            try:
                last_called = debounced.last_called
            except AttributeError:
                last_called = 0
            if current_time - last_called >= wait:
                fn(*args, **kwargs)
                debounced.last_called = current_time
        return debounced
    return decorator

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
        
        self.build_search_form()
        
        self.rooms_frame = tk.Frame(self)
        self.rooms_frame.pack(fill=tk.BOTH, expand=True)
        
        self.preload_images_async()

        self.checkin_var = tk.StringVar(value="Check-in Date: None")
        self.checkout_var = tk.StringVar(value="Check-out Date: None")
        tk.Label(self, textvariable=self.checkin_var, font=("Helvetica", 12), fg="green").pack(pady=2)
        tk.Label(self, textvariable=self.checkout_var, font=("Helvetica", 12), fg="green").pack(pady=2)

    def preload_images_async(self):
        thread = threading.Thread(target=self.preload_images, daemon=True)
        thread.start()

    def preload_images(self):
        for room in ROOMS:
            path = room["image"]
            try:
                img = Image.open(path).resize((100, 100), Image.ANTIALIAS)
                self.images[room["name"]] = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Error preloading image {path}: {e}")

    def build_search_form(self):
        search_frame = tk.Frame(self)
        search_frame.pack(pady=10, fill=tk.X)

        tk.Label(search_frame, text="Location:").pack(side=tk.LEFT, padx=5)
        self.location_var = tk.StringVar()
        location_dropdown = ttk.Combobox(search_frame, textvariable=self.location_var, values=LOCATIONS, state="readonly")
        location_dropdown.pack(side=tk.LEFT, padx=5)
        location_dropdown.set("Select Location")

        tk.Label(search_frame, text="Check-in:").pack(side=tk.LEFT, padx=5)
        tkmacosx.Button(search_frame, text="Select Date", command=self.debounce_select_date('checkin')).pack(side=tk.LEFT, padx=5)

        tk.Label(search_frame, text="Check-out:").pack(side=tk.LEFT, padx=5)
        tkmacosx.Button(search_frame, text="Select Date", command=self.debounce_select_date('checkout')).pack(side=tk.LEFT, padx=5)

        tkmacosx.Button(search_frame, text="Search", command=self.display_rooms).pack(side=tk.LEFT, padx=10)

    def debounce_select_date(self, date_type):
        @debounce(0.3)  # Adjust debounce time as needed
        def wrapped():
            self.select_date(date_type)
        return wrapped

    @debounce(0.3)  # Adjust debounce time as needed
    def display_rooms(self):
        for widget in self.rooms_frame.winfo_children():
            widget.destroy()
        for room in ROOMS:
            self.add_room_listing(room)


    def select_date(self, date_type):
        dialog = CalendarDialog(self)
        if dialog.result:
            formatted_date = dialog.result
            if date_type == 'checkin':
                self.checkin_var.set(f"Check-in Date: {formatted_date}")
            elif date_type == 'checkout':
                self.checkout_var.set(f"Check-out Date: {formatted_date}")

    def add_room_listing(self, room):
        room_frame = tk.Frame(self.rooms_frame, borderwidth=2, relief=tk.GROOVE)
        room_frame.pack(pady=10, padx=10, fill=tk.X)

        image = self.images.get(room["name"], None)
        if image:
            img_label = tk.Label(room_frame, image=image)
            img_label.pack(side=tk.LEFT, padx=5)
        else:
            tk.Label(room_frame, text="Image not found", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)

        tk.Label(room_frame, text=room["name"], font=("Helvetica", 16)).pack(side=tk.LEFT, padx=5)
        tk.Label(room_frame, text=f"Price: {room['price']}", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)

        tkmacosx.Button(room_frame, text="Book Room", command=lambda room=room: self.book_room(room)).pack(side=tk.RIGHT, padx=10)

    def book_room(self, room):
        print(f"Booking {room['name']}...")