import tkinter as tk
from tkinter import font
from page import Page

class Policies(Page):
    """
    This class represents the policies page in the application, where various hotel policies are displayed.

    :author: Arameh Baghdasarian
    :version: 2.0

    Attributes:
        policiesText (tk.Text): A text widget to display hotel policies.
    
    Methods:
        insert_policy(header, policy): Inserts a policy with a given header and content.
    """

    def __init__(self, parent, controller):
        """
        Initializes the Policies page.

        Args:
            parent (tk.Widget): The parent widget for the policies page.
            controller (object): The controller object for managing page navigation.
        """
        super().__init__(parent, controller)
        
        # Create the header for the policies page
        headerFont = ("Arial", 32, "bold", "underline")
        headerLabel = tk.Label(self, text="POLICIES", font=headerFont, bg="white", fg="black", pady=10)
        headerLabel.pack(side="top", fill="x", anchor="center")

        # Create a frame for the policies text and scrollbar
        textFrame = tk.Frame(self)
        textFrame.pack(fill="both", expand=True)
        
        # Create the Text widget for displaying policies
        self.policiesText = tk.Text(textFrame, wrap="word", font=("Arial", 15), bg="white", fg="black", bd=0, highlightthickness=0, padx=20, pady=30)
        
        # Create a Scrollbar widget for the text area
        scrollbar = tk.Scrollbar(textFrame, command=self.policiesText.yview)
        self.policiesText.configure(yscrollcommand=scrollbar.set)
        
        # Pack the scrollbar on the right side and fill vertically
        scrollbar.pack(side="right", fill="y")
        
        # Pack the Text widget to fill the remaining space
        self.policiesText.pack(side="left", fill="both", expand=True)

        # Define a bold font for emphasizing text
        boldFont = font.Font(self.policiesText, self.policiesText.cget("font"))
        boldFont.configure(weight="bold")
        
        # Configure a tag for bold text
        self.policiesText.tag_configure("bold", font=boldFont)
        
        # Insert various hotel policies into the text widget
        self.insert_policy("Check-in and Check-out Policy:", """
Guests are invited to check in anytime after 2:00 PM on their day of arrival and are kindly asked to check out by 11:00 AM on their departure day. Early check-ins and late check-outs can be accommodated upon request, subject to availability, and may incur additional charges. Please contact the front desk 24 hours prior to your arrival or departure to make these arrangements.
""")

        self.insert_policy("Updating Booking Policy:", """
Guests are allowed to update their booking details, including dates of stay and room type, up to 72 hours before the scheduled check-in time, free of charge. Any changes made within 72 hours of arrival are subject to availability and may incur a fee. To update your booking, please log into your account, select the reservation you would like to update, edit your reservation, and confirm.
""")

        self.insert_policy("Cancellation Policy:", """
Reservations can be cancelled free of charge within 72 hours of creating the initial booking. Cancellations made after this period will incur a charge equivalent to one night's stay. To cancel your booking, select the reservation you would like to cancel, select “Cancel”, and confirm.
""")

        self.insert_policy("Cancellation By Hotel:", """
In the rare event that we must cancel a booking due to unforeseen circumstances, our hotel will provide guests with immediate notification and offer a full refund or the option to rebook on alternative dates, subject to availability. We reserve the right to cancel a booking without refund for reasons that necessitate such action. These include violation of hotel policy (engaging in illegal activities, causing severe disruption, or presenting safety concerns), and fraud.
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

        # Disable editing on the policies text widget
        self.policiesText.config(state="disabled")

    def insert_policy(self, header, policy):
        """
        Inserts a policy with a given header and content into the text widget.

        Args:
            header (str): The header or title of the policy.
            policy (str): The content of the policy.
        """
        self.policiesText.config(state="normal")  # Temporarily enable editing to insert text
        self.policiesText.insert("end", f"{header}\n", "bold")
        self.policiesText.insert("end", f"{policy}\n")
        self.policiesText.config(state="disabled")  # Disable editing after insertion

        self.update_idletasks()
