import unittest
from unittest.mock import MagicMock, patch
from hotelsView import HotelsView

class TestHotelsView(unittest.TestCase):
    """
    Tests the HotelsView class to validate the proper display and interaction of hotel data.
    Focuses on the functionality of displaying hotels, handling images, and room availability checks.

    Author: Gurnoor Kaur
    Version: 1.0
    """

    def setUp(self):
        """
        Set up the test environment before each test by initializing the HotelsView with mock data.
        Mocks are used to simulate the database and image handling to focus on the logic rather than external dependencies.
        """
        self.controller = MagicMock()

        self.hotels = [
            {'hotelName': 'Hotel One', 'photoLink': 'path/to/hotel_one.jpg', 'price_range': '$100-$200', 'amenities': ['Free WiFi', 'Parking']},
            {'hotelName': 'Hotel Two', 'photoLink': 'path/to/hotel_two.jpg', 'price_range': '$150-$300', 'amenities': ['Pool', 'Spa']}
        ]

        with patch('tkinter.Label'), patch('PIL.ImageTk.PhotoImage'):
            self.hotelsView = HotelsView(None, self.controller, self.hotels, "2024-01-01", "2024-01-05")

    @patch('PIL.Image.open')
    @patch('PIL.ImageTk.PhotoImage')
    def testDisplayHotels(self, mock_photo_image, mock_open):
        """
        Tests the displayHotels method to ensure it successfully creates image components for hotels.
        Mocks image processing to verify method logic without actual file I/O.
        """
        mock_image = MagicMock()
        mock_open.return_value = mock_image
        mock_image.resize.return_value = mock_image
        mock_photo_image.return_value = MagicMock()

        self.hotelsView.displayHotels()
        mock_open.assert_called()
        self.assertTrue(mock_photo_image.called)

    @patch('tkinter.messagebox.showinfo')
    def testShowRooms(self, mock_showinfo):
        """
        Tests the showRooms method to verify it correctly handles room availability queries.
        Uses mock message boxes to confirm the interaction with the user interface when no rooms are available.
        """
        self.hotelsView.db = MagicMock()
        self.hotelsView.db.fetchRoomByHotelAvail.return_value = []
        self.hotelsView.showRooms('Hotel One', '2024-01-01', '2024-01-05')
        mock_showinfo.assert_called_once_with("Rooms", "No available rooms for the selected dates.")

if __name__ == '__main__':
    unittest.main()
