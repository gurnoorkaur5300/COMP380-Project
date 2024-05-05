import tkinter as tk
from tkinter import ttk,  messagebox
from PIL import Image, ImageTk
from database import Database
from page import Page
from room import Room


LOCATIONS = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]


class HotelsView(Page):
    """
    This class represents the page displaying available hotels.
    
    Author: Gregory Calderon and Gurnoor Kaur
    
    Attributes:
        parent: The parent widget to which the hotels view page belongs.
        controller: The controller object responsible for managing page navigation.
        db: The database object for accessing hotel and room information.
        hotels: A list of dictionaries containing hotel information.
        checkIn: The check-in date.
        checkOut: The check-out date.
        hotelsFrame: The frame containing the hotels view.
        contentFrame: The frame containing hotel information.
        canvas: The canvas widget for scrolling hotel information.
        innerFrame: The frame inside the canvas for displaying hotel information.

    Methods:
        setHotelsData(n_hotelData, n_checkIn, n_checkOut): Sets the hotel data and check-in/check-out dates.
        displayHotels(): Displays the available hotels.
        populateHotels(): Populates the hotels view with hotel information.
        showRooms(hotelName, checkin, checkout): Displays available rooms for a selected hotel.
        onCanvasConfigure(event): Configures the canvas widget for scrolling.
    """
    def __init__(self, parent, controller, n_hotelData=None, n_checkIn=None, n_checkOut=None):
        super().__init__(parent, controller)
        self.db = Database()  
        
        self.controller = controller
        self.hotels = n_hotelData
        self.checkIn = n_checkIn
        self.checkOut = n_checkOut
        
        if self.hotels is not None:
            self.displayHotels()
            
    def setHotelsData(self, n_hotelData, n_checkIn, n_checkOut):
        self.hotels = n_hotelData
        self.checkIn = n_checkIn
        self.checkOut = n_checkOut
        
    def displayHotels(self):
        
        self.hotelsFrame = tk.Frame(self, bg='white')
        self.hotelsFrame.pack(fill=tk.BOTH, expand=True)
        
        self.contentFrame = tk.Frame(self.hotelsFrame, bg='white')
        self.contentFrame.pack(fill=tk.BOTH, expand=True,side=tk.LEFT)
        
        self.canvas = tk.Canvas(self.contentFrame, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.onCanvasConfigure)
       
        self.innerFrame = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window((0, 0), window=self.innerFrame, anchor="nw")


        scrollbar = ttk.Scrollbar(self.hotelsFrame, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.populateHotels()

    def populateHotels(self):
        for hotel in self.hotels:
            self.hotelFrame = tk.Frame(self.innerFrame, borderwidth=2, relief="solid", padx =50, pady=20)
            self.hotelFrame.pack(pady=10, fill=tk.X)
                 
            # print(hotel)
            photoPath = hotel['photoLink']
            try:
                image = Image.open(photoPath)
                image = image.resize((100, 100))
                img = ImageTk.PhotoImage(image)
                img_label = tk.Label(self.hotelFrame, image=img)
                img_label.image = img
                img_label.pack(side=tk.LEFT, padx=10)
            except Exception as e:
                print("Error opening or resizing image:", e)
            

            self.hotelInfo = f"{hotel['hotelName']} - {hotel['price_range']}\nAmenities: {', '.join(hotel['amenities'])}"
            self.hotelLabel = tk.Label(self.hotelFrame, text=self.hotelInfo, justify=tk.LEFT)
            self.hotelLabel.pack(side=tk.LEFT, padx=10)

            showRoomsButton = ttk.Button(self.hotelFrame, text="Show Rooms", command=lambda hotelName=hotel['hotelName']: self.showRooms(hotelName, self.checkIn, self.checkOut))
            showRoomsButton.pack(side=tk.RIGHT, padx=10)

    def showRooms(self, hotelName, checkin, checkout):
        rooms = self.db.fetchRoomByHotelAvail(hotelName, checkin, checkout)
        for room in rooms:
            print(room)
        if not rooms:
            messagebox.showinfo("Rooms", "No available rooms for the selected dates.")
            return
        #line added to clear the rooms page every time there is a new search
        self.controller.room.clearRooms()
        self.controller.room.setRooms(rooms, checkin, checkout)
        self.controller.room.displayRooms()
        self.controller.showFrame("Room")


    def clearHotels(self):
        """
        Clear all the widgets related to displaying hotels.
        """
        if hasattr(self, 'hotelsFrame'):
            self.hotelsFrame.destroy()    


    def onCanvasConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))