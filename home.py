import tkinter as tk
from page import Page
from tkinter import ttk
from tkcalendar import Calendar, DateEntry  # Ensure you have tkcalendar installed (`pip install tkcalendar`)

class Home(Page):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        # Title Label
        title = tk.Label(self, text="Welcome to Titan Reservations", font=("Helvetica", 24))
        title.pack(pady=20)
        
        # Search Frame for inputs
        search_frame = tk.Frame(self)
        search_frame.pack(pady=10)
        
        # Location Entry
        tk.Label(search_frame, text="Location:").grid(row=0, column=0, padx=5, pady=5)
        location_entry = tk.Entry(search_frame)
        location_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Check-in Date Picker
        tk.Label(search_frame, text="Check-in:").grid(row=1, column=0, padx=5, pady=5)
        checkin_date = DateEntry(search_frame, width=17, background='darkblue',
                                 foreground='white', borderwidth=2)
        checkin_date.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Check-out Date Picker
        tk.Label(search_frame, text="Check-out:").grid(row=2, column=0, padx=5, pady=5)
        checkout_date = DateEntry(search_frame, width=17, background='darkblue',
                                   foreground='white', borderwidth=2)
        checkout_date.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        # Search Button
        search_btn = tk.Button(search_frame, text="Search", command=lambda: self.search_hotels(location_entry.get(), checkin_date.get_date(), checkout_date.get_date()))
        search_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Configure the grid
        search_frame.columnconfigure(1, weight=1)
        
        # Listings Label - Placeholder for search results
        self.listings_label = tk.Label(self, text="Search results will appear here", font=("Helvetica", 14))
        self.listings_label.pack(pady=20)
        
        # Example Navigation Buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        policies_btn = tk.Button(btn_frame, text="View Policies", command=lambda: controller.showFrame("Policies"))
        policies_btn.pack(side=tk.LEFT, padx=10)
        
        # More buttons can be added here following the same pattern
        
    def search_hotels(self, location, checkin, checkout):
        # Placeholder for search logic
        self.listings_label.configure(text=f"Search for hotels in {location} from {checkin} to {checkout}")
