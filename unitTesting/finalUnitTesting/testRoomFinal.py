import unittest
import tkinter as tk
from unittest.mock import MagicMock
from room import Room

class TestRoom(unittest.TestCase):
    """
    Tests the Room class to ensure proper functionality
    :author: Arameh Baghdasarian
    :version: 1.0
    """
    def setUp(self):
        self.root = tk.Tk()
        self.controller = MagicMock()
        self.room_page = Room(self.root, self.controller)
        self.room_page.pack()  

    def testSetRooms(self):
        rooms = [{'roomId': '101', 'roomNum': '101', 'hotelName': 'Test Hotel', 'location': 'Test City', 'cost': 200.0}]
        checkIn = '2024-05-15'
        checkOut = '2024-05-20'
        
        self.room_page.setRooms(rooms, checkIn, checkOut)
        
        self.assertEqual(self.room_page._Room__rooms, rooms)
        self.assertEqual(self.room_page._Room__checkIn, checkIn)
        self.assertEqual(self.room_page._Room__checkOut, checkOut)

    def testDisplayRooms(self):
        self.room_page.setRooms(
            [{'roomId': '101', 'roomNum': '101', 'hotelName': 'Test Hotel', 'location': 'Test City', 'cost': 200.0}],
            '2024-05-15',
            '2024-05-20'
        )
        self.room_page.displayRooms()

        self.assertTrue(hasattr(self.room_page, 'roomsFrame'))
        self.assertTrue(hasattr(self.room_page, 'contentFrame'))
        self.assertTrue(hasattr(self.room_page, 'canvas'))
        self.assertTrue(hasattr(self.room_page, 'innerFrame'))

    def testPopulateRooms(self):
        rooms = [
            {'roomId': '101', 'roomNum': '101', 'hotelName': 'Test Hotel', 'location': 'Test City', 'cost': 200.0},
            {'roomId': '102', 'roomNum': '102', 'hotelName': 'New Hotel', 'location': 'New City', 'cost': 300.0}
        ]
        self.room_page.setRooms(rooms, '2024-05-15', '2024-05-20')
        self.room_page.displayRooms()
        self.room_page.populateRooms()

        children = self.room_page.innerFrame.winfo_children()
        self.assertEqual(len(children), 2)

    def testBookRoom(self):
        self.controller.isLoggedIn = True
        self.room_page.setCustomerName("John Doe")
        self.room_page.setCustomerId("123")
        self.room_page.setCustomerEmail("john.doe@example.com")

        self.room_page.bookRoom('101', '101', 'Test Hotel', 'Test City', 200.0)

        self.controller.viewReservation.setCustomerName.assert_called_with("John Doe")
        self.controller.viewReservation.setCustomerId.assert_called_with("123")
        self.controller.viewReservation.setCustomerEmail.assert_called_with("john.doe@example.com")
        self.controller.showFrame.assert_called_with("ViewReservation")

    def testClearRooms(self):
        self.room_page.setRooms(
            [{'roomId': '101', 'roomNum': '101', 'hotelName': 'Test Hotel', 'location': 'Test City', 'cost': 200.0}],
            '2024-05-15',
            '2024-05-20'
        )
        self.room_page.displayRooms()
        self.room_page.clearRooms()

        self.assertFalse(hasattr(self.room_page, 'roomsFrame'))

if __name__ == '__main__':
    unittest.main()
