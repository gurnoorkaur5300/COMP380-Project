import unittest
from unittest.mock import MagicMock, patch
from home import Home
from tkinter import messagebox

class TestHome(unittest.TestCase):
    """
    Tests the Home class to ensure proper functionality.
    This suite aims to validate the behavior of key functionalities within the Home page,
    focusing on date selection, search initiation, and database interaction handling.

    :author: Gurnoor Kaur
    :version: 1.0
    """

    def setUp(self):
        """
        Set up the test environment before each test.
        Mocks the controller and initializes the Home page with this mocked controller.
        The Home class is responsible for handling user inputs for travel and accommodations searching.

        Attributes setup:
        - controller: A MagicMock object to simulate the controller managing page transitions.
        - homePage: The instance of the Home class being tested, initialized with the mocked controller.
        """
        self.controller = MagicMock()
        self.homePage = Home(None, self.controller)

    def testSelectDate(self):
        """
        Tests the selectDate method to verify if the correct date is being set for check-in and check-out.
        The method should correctly interpret the date picked from a CalendarDialog and set it in the relevant variable.
        """
        with patch('home.CalendarDialog') as MockCalendarDialog:
            # Mock the CalendarDialog to return a specific date when the calendar is used.
            mock_dialog = MockCalendarDialog.return_value
            mock_dialog.result = MagicMock()
            mock_dialog.result.strftime.return_value = '2024-05-01'

            self.homePage.selectDate('checkin')
            self.assertEqual(self.homePage.checkinVar.get(), '2024-05-01')
            self.homePage.selectDate('checkout')
            self.assertEqual(self.homePage.checkoutVar.get(), '2024-05-01')

    def testStartSearch(self):
        """
        Tests the start_search method to ensure it starts the search operation in a separate thread.
        This method is critical for responsive UI, allowing database queries to be handled asynchronously.
        """
        with patch('threading.Thread') as mock_thread:
            self.homePage.start_search()
            mock_thread.assert_called_once()

    def testSearch(self):
        """
        Tests the search method to ensure it interacts properly with the database and correctly handles the flow of data.
        This method checks the interaction with the database to fetch hotels by location and the subsequent handling of that data,
        ensuring correct page transitions and error handling if no data is found.

        Mocks:
        - fetchHotelsByLocation: Simulates fetching hotel data based on the location provided by the user.
        - showFrame: Simulates the transition to the HotelsView page if hotels data exists.
        """
        self.homePage.db = MagicMock()
        self.homePage.controller = MagicMock()

        # No hotels found scenario
        self.homePage.db.fetchHotelsByLocation.return_value = None
        self.homePage.locationVar.set("Chicago")
        self.homePage.checkinVar.set("2024-06-01")
        self.homePage.checkoutVar.set("2024-06-10")
        self.homePage.search()
        
        self.homePage.db.fetchHotelsByLocation.assert_called_with("Chicago")
        self.assertTrue(self.homePage.db.fetchHotelsByLocation.called)
        self.homePage.controller.showFrame.assert_not_called()

        # Hotels found scenario
        self.homePage.db.fetchHotelsByLocation.return_value = ['Hotel 1', 'Hotel 2']
        self.homePage.search()
        self.homePage.controller.showFrame.assert_called_once_with("HotelsView")

if __name__ == '__main__':
    unittest.main()
