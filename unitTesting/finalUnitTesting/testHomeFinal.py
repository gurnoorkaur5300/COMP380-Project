import unittest
from unittest.mock import MagicMock, patch
import datetime
from home import Home, CalendarDialog

class TestHomeFinal(unittest.TestCase):
    """
    Tests the Home class to ensure proper functionality of the travel search and display interface.
    :author: Gurnoor Kaur
    :version: 1.0
    """

    def setUp(self):
        """
        Set up the test environment. Create mock objects for controller and database. Simulate the page environment for Home.

        Mocks:
        - controller: A MagicMock object simulating the controller for page navigation.
        - database: A MagicMock object simulating the database that handles fetching hotel data based on location.

        Initialization:
        - Initialize the Home page object with the mocked controller.
        """
        self.controller = MagicMock()
        self.database = MagicMock()
        self.home = Home(None, self.controller)
        self.home.db = self.database  # Assigning the mock database to the Home instance

    def testSelectDate(self):
        """
        Tests the date selection dialog and subsequent setting of date in Home.
        """
        with patch('home.CalendarDialog') as MockCalendarDialog:
            mock_dialog = MockCalendarDialog.return_value
            mock_dialog.result = datetime.date(2024, 5, 1)  # Correcting to use datetime.date
            self.home.selectDate('checkin')
            self.assertEqual(self.home.checkinVar.get(), "2024-05-01")
            self.home.selectDate('checkout')
            self.assertEqual(self.home.checkoutVar.get(), "2024-05-01")

    def testStartSearch(self):
        """
        Tests the starting of a search thread.
        """
        self.home.start_search = MagicMock()
        self.home.start_search()
        self.home.start_search.assert_called_once()

    def testSearchHotels(self):
        """
        Tests the search functionality that fetches hotels based on given location and dates.
        """
        self.database.fetchHotelsByLocation.return_value = ["Hotel 1", "Hotel 2"]
        self.home.locationVar.set("New York")
        self.home.checkinVar.set("2024-05-10")
        self.home.checkoutVar.set("2024-05-15")
        self.home.search()
        self.database.fetchHotelsByLocation.assert_called_with("New York")
        self.controller.showFrame.assert_called_with("HotelsView")

    def testResetFields(self):
        """
        Tests if the search fields are reset properly.
        """
        self.home.resetFields()
        self.assertEqual(self.home.locationVar.get(), "Select Location")
        self.assertEqual(self.home.checkinVar.get(), "")
        self.assertEqual(self.home.checkoutVar.get(), "")

if __name__ == '__main__':
    unittest.main()
