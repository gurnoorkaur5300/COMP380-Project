import tkinter as tk
from tkinter import font
from page import Page

class Policies(Page):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        # create the header
        headerFont = ("Arial", 32, "bold", "underline")
        headerLabel = tk.Label(self, text="HOTEL POLICIES", font=headerFont)
        headerLabel.pack(side="top", fill="x", pady=(10, 20), anchor="center")

        # Creating a frame for the policies text and scrollbar
        textFrame = tk.Frame(self)
        textFrame.pack(pady=30, fill="both", expand=True)
        
        # Creating the Text widget
        self.policiesText = tk.Text(textFrame, wrap="word", font=("Arial", 15), bg="white", bd=0, highlightthickness=0, padx=150, pady = 30)
        
        # Creating a Scrollbar widget
        scrollbar = tk.Scrollbar(textFrame, command=self.policiesText.yview)
        self.policiesText.configure(yscrollcommand=scrollbar.set)
        
        # Packing the scrollbar to the right side and filling y-axis
        scrollbar.pack(side="right", fill="y")
        
        # Packing the Text widget to fill both axes
        self.policiesText.pack(side="left", fill="both", expand=True)

        # Defining a bold font
        boldFont = font.Font(self.policiesText, self.policiesText.cget("font"))
        boldFont.configure(weight="bold")
        
        # Creating a tag for bold text
        self.policiesText.tag_configure("bold", font=boldFont)
        


        # Adding policies
        self.insert_policy("Check-in and Check-out Policy:", """
Guests are invited to check in anytime after 2:00 PM on their day of arrival and are kindly asked to check out by 11:00 AM on their departure day. Early check-ins and late check-outs can be accommodated upon request, subject to availability and may incur additional charges. Please contact the front desk 24 hours prior to your arrival or departure to make these arrangements.
""")

        self.insert_policy("Updating Booking Policy:", """
Guests are allowed to update their booking details, including dates of stay and room type, up to 72 hours before the scheduled check-in time, free of charge. Any changes made within 72 hours of arrival are subject to availability and may incur a fee. To update your booking, please log into your account, select the reservation you would like to update, edit your reservation, and confirm.
""")
        self.insert_policy("Cancellation Policy:", """
Reservations can be cancelled free of charge within 72 hours of creating the initial booking. Cancellations made after this period will incur a charge equivalent to one night's stay. To cancel your booking, select the reservation you would like to cancel, select “Cancel”, and confirm.

""")
        self.insert_policy("Cancellation By Hotel:", """
In the rare event that we must cancel a booking due to unforeseen circumstances, our hotel will provide guests with immediate notification and offer a full refund or the option to rebook on alternative dates, subject to availability. 
We reserve the right to cancel a booking without refund for reasons that necessitate such action. These include violation of hotel policy (engaging in illegal activities, causing severe disruption, or presenting safety concerns) and fraud.

""")
        self.insert_policy("Is My Booking Refundable?:", """
All bookings made directly through our official website or reservations team are considered refundable as per our cancellation policy. Bookings made via third-party platforms may be subject to different terms and conditions. Please refer to your booking confirmation to verify the refundability of your reservation.

""")
        self.insert_policy("Smoking Policy:", """
Our hotel is committed to providing a healthy and comfortable environment for all guests and staff. Therefore, smoking is strictly prohibited in all indoor areas, including guest rooms. Designated smoking areas are available outside the hotel building. Violation of this policy will result in a cleaning fee charged to the offending guest's account, or in the case of repeat offenses, cancellation of the offender’s reservation with no refund.

""")
        self.insert_policy("Damage Policy:", """
Guests are responsible for any damage caused to the room or hotel property during their stay. Charges for repair or replacement will be assessed and added to the guest's bill. We encourage guests to report any accidental damage to the front desk as soon as possible.

""")
        self.insert_policy("Accessibility:", """
We offer a range of accessible guest rooms equipped with features like wheelchair-accessible doorways, ramps to get in and out of the building, and elevators. Please contact our reservations team to discuss any specific accessibility requirements.

""")

        # Ensure user cant edit text widget
        self.policiesText.config(state="disabled")

    def insert_policy(self, header, policy):
        self.policiesText.config(state="normal")  # Temporarily enable editing to insert text
        self.policiesText.insert("end", f"{header}\n", "bold")
        self.policiesText.insert("end", f"{policy}\n")
        self.policiesText.config(state="disabled")  # Disable editing after insertion

    def __init__(self,parent,controller):
        super().__init__(parent,controller)
        label = tk.Label(self, text="Policies is Alive")
        label.pack()

        self.update_idletasks()

