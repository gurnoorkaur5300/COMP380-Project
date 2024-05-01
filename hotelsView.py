import tkinter as tk
from tkinter import ttk,  messagebox
from PIL import Image, ImageTk
from database import Database
from page import Page


LOCATIONS = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]


class HotelsView(Page):
    def __init__(self, parent, controller, database, n_hotelData=None, n_checkIn=None, n_checkOut=None):
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
            

            self.hotelInfo = f"{hotel['name']} - {hotel['price_range']}\nAmenities: {', '.join(hotel['amenities'])}"
            self.hotelLabel = tk.Label(self.hotelFrame, text=self.hotelInfo, justify=tk.LEFT)
            self.hotelLabel.pack(side=tk.LEFT, padx=10)

            showRoomsButton = ttk.Button(self.hotelFrame, text="Show Rooms", command=lambda hotelName=hotel['name']: self.showRooms(hotelName, self.checkIn, self.checkOut))
            showRoomsButton.pack(side=tk.RIGHT, padx=10)
            
        
    

    def showRooms(self, hotelName, checkin, checkout):
        rooms = self.db.fetchRoomByHotelAvail(hotelName, checkin, checkout)
        for room in rooms:
            print(room)
        if not rooms:
            messagebox.showinfo("Rooms", "No available rooms for the selected dates.")
            return
        messagebox.showinfo("Rooms", f"Available rooms for {hotelName}:\n" + '\n'.join([f"Room {room['roomNum']} at ${room['cost']}" for room in rooms]))

    

    def onCanvasConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))