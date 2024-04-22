import tkinter as tk
from tkinter import ttk, simpledialog, font, messagebox
from PIL import Image, ImageTk
from tkcalendar import Calendar
from page import Page
from tkmacosx import Button  
from hotels import Hotels  
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
        title = tk.Label(self, text="Share Your Travel Dates, and We'll Handle the Rest!", font=titleFont, fg="#003366")
        title.pack(pady=30)

        self.buildSearchForm()
        self.addQuotes()

    def setupBackground(self):
        self.bgImage = Image.open('assets/bk.jpeg')  
        self.bgPhoto = ImageTk.PhotoImage(self.bgImage)
        bgLabel = tk.Label(self, image=self.bgPhoto)
        bgLabel.place(relwidth=1, relheight=1, x=0, y=0)

    def buildSearchForm(self):
        searchFrame = tk.Frame(self, bg='white', borderwidth=2, relief="solid", padx=45, pady=20)
        searchFrame.pack(pady=60, padx=100)

        tk.Label(searchFrame, text="Destination:", bg='white', font=("Arial", 16)).pack(pady=10)
        self.locationVar = tk.StringVar()
        locationDropdown = ttk.Combobox(searchFrame, textvariable=self.locationVar, values=LOCATIONS, state="readonly", font=("Arial", 14))
        locationDropdown.pack(pady=10)
        locationDropdown.set("Select Location")

        tk.Label(searchFrame, text="Check-in Date:", bg='white', font=("Arial", 16)).pack(pady=10)
        self.checkinVar = tk.StringVar()
        self.checkinEntry = tk.Entry(searchFrame, textvariable=self.checkinVar, width=20, font=("Arial", 14))
        self.checkinEntry.pack(pady=10)
        self.checkinEntry.bind("<Button-1>", lambda event: self.selectDate('checkin'))

        tk.Label(searchFrame, text="Check-out Date:", bg='white', font=("Arial", 16)).pack(pady=10)
        self.checkoutVar = tk.StringVar()
        self.checkoutEntry = tk.Entry(searchFrame, textvariable=self.checkoutVar, width=20, font=("Arial", 14))
        self.checkoutEntry.pack(pady=10)
        self.checkoutEntry.bind("<Button-1>", lambda event: self.selectDate('checkout'))

        Button(searchFrame, text="Search Rooms", command=self.start_search_thread, bg="#003366", fg="white", font=("Arial", 18)).pack(pady=30)

    def selectDate(self, dateType):
        dialog = CalendarDialog(self)
        if dialog.result:
            formattedDate = dialog.result.strftime("%Y-%m-%d")
            if dateType == 'checkin':
                self.checkinVar.set(formattedDate)
            elif dateType == 'checkout':
                self.checkoutVar.set(formattedDate)

    def start_search_thread(self):
        # new thread to not have indefinite loading
        threading.Thread(target=self.search, daemon=True).start()

    # def search(self):
    #     checkinDate = self.checkinVar.get()
    #     checkoutDate = self.checkoutVar.get()
    #     location = self.locationVar.get()
    #     destination_id = Hotels.get_destination_id(location)
    #     if destination_id:
    #         hotel_data = Hotels.fetch_hotels(destination_id, checkinDate, checkoutDate)
    #         self.show_hotels(hotel_data)
    #     else:
    #         self.after(0, lambda: messagebox.showerror("Error", "Failed to find the destination. Please try again."))
    
    def search(self):
        checkinDate = self.checkinVar.get()
        checkoutDate = self.checkoutVar.get()
        location = self.locationVar.get()
    
        if not location or location == "Select Location":
            messagebox.showerror("Error", "Please select a valid location.")
            return
    
        destination_id = Hotels.get_destination_id(location)
        if destination_id:
            hotel_data = Hotels.fetch_hotels(destination_id, checkinDate, checkoutDate)
            if hotel_data:
                self.controller.after(0, lambda: self.show_hotels(hotel_data))
            else:
                self.controller.after(0, lambda: messagebox.showerror("Search Failed", "Could not retrieve hotel data."))
        else:
            self.controller.after(0, lambda: messagebox.showerror("Error", "Failed to find the destination. Please try again."))
    
    
    def show_hotels(self, hotel_data):
        # must be called on the main thread
        if 'data' in hotel_data:
            top = tk.Toplevel(self)
            top.title("Available Rooms")
            for hotel in hotel_data['data']['body']['searchResults']['results']:
                tk.Label(top, text=f"{hotel['name']} - {hotel['ratePlan']['price']['current']}", font=("Arial", 14)).pack()
            top.mainloop()
        else:
            messagebox.showerror("Search Failed", "Could not retrieve hotel data.")

    def addQuotes(self):
        quotesFrame = tk.Frame(self, bg='white', borderwidth=0)
        quotesFrame.pack(pady=10, fill=tk.X)
        quote2 = tk.Label(quotesFrame, text="To Travel is to Live!", bg='white', fg="#003366", font=("Georgia", 24, "italic"))
        quote2.pack()
