import tkinter as tk
from tkinter import ttk, simpledialog, font, messagebox
from tkcalendar import Calendar
from page import Page
from hotels import Hotels

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
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.build_search_form()

    def build_search_form(self):
        self.title = tk.Label(self, text="Welcome to Titan Reservations", font=self.title_font, fg="blue")
        self.title.pack(pady=20)

        self.search_frame = tk.Frame(self)
        self.search_frame.pack(pady=10, fill=tk.X)

        tk.Label(self.search_frame, text="Location:").pack(side=tk.LEFT, padx=5)
        self.location_var = tk.StringVar()
        self.location_dropdown = ttk.Combobox(self.search_frame, textvariable=self.location_var, values=["New York", "Los Angeles", "Chicago", "Houston", "Miami"], state="readonly")
        self.location_dropdown.pack(side=tk.LEFT, padx=5)
        self.location_dropdown.set("Select Location")

        tk.Label(self.search_frame, text="Check-in:").pack(side=tk.LEFT, padx=5)
        self.checkin_var = tk.StringVar()
        self.checkin_entry = tk.Entry(self.search_frame, textvariable=self.checkin_var, width=15)
        self.checkin_entry.pack(side=tk.LEFT, padx=5)
        self.checkin_entry.bind("<Button-1>", lambda event: self.select_date('checkin'))

        tk.Label(self.search_frame, text="Check-out:").pack(side=tk.LEFT, padx=5)
        self.checkout_var = tk.StringVar()
        self.checkout_entry = tk.Entry(self.search_frame, textvariable=self.checkout_var, width=15)
        self.checkout_entry.pack(side=tk.LEFT, padx=5)
        self.checkout_entry.bind("<Button-1>", lambda event: self.select_date('checkout'))

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search)
        self.search_button.pack(side=tk.LEFT, padx=10)

    def select_date(self, date_type):
        dialog = CalendarDialog(self)
        self.wait_window(dialog)  # Wait for the dialog to close before proceeding
    
        if hasattr(dialog, 'result') and dialog.result:
            formatted_date = dialog.result.strftime("%Y-%m-%d")
            if date_type == 'checkin':
                self.checkin_var.set(formatted_date)
            elif date_type == 'checkout':
                self.checkout_var.set(formatted_date)
    

         

    def display_results(self, results):
        result_window = tk.Toplevel(self)
        result_window.title("Search Results")
        tree = ttk.Treeview(result_window, columns=("Name", "Price", "Rating"), show="headings")
        tree.heading("Name", text="Name")
        tree.heading("Price", text="Price")
        tree.heading("Rating", text="Rating")

        if results.get('hotels'):
            for hotel in results['hotels']:
                tree.insert("", "end", values=(hotel["name"], hotel["price"], hotel["rating"]))

        tree.pack(expand=True, fill="both")

    def search(self):
        location_name = self.location_var.get()
        checkin_date = self.checkin_var.get()
        checkout_date = self.checkout_var.get()
        if location_name and checkin_date and checkout_date:
            destination_id = Hotels.get_destination_id(location_name)
            if destination_id:
                result = Hotels.fetch_hotels(destination_id, checkin_date, checkout_date)
                if 'error' in result:
                    messagebox.showerror("Error", result['error'])
                elif 'hotels' in result and result['hotels']:
                    self.display_results(result)
                else:
                    messagebox.showinfo("No Results", "No hotels found. Please try different dates or another location.")
            else:
                messagebox.showerror("Error", "Failed to get destination ID. Please try a different location.")
        else:
            messagebox.showerror("Error", "Please complete all fields.")
if __name__ == "__main__":
    root = tk.Tk()
    app = Home(root, None)
    app.pack(expand=True, fill="both")
    root.mainloop()

