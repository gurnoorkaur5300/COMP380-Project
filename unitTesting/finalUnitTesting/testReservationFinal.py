import unittest
from reservation import Reservation  # Assuming the class is saved in a file named reservation.py

class TestReservation(unittest.TestCase):
    """
    Tests the Reservation class to ensure proper functionality
    :author: Martin Gallegos Cordero
    :version: 1.0
    """

    def setUp(self):
        self.reservation = Reservation(
            n_customerId="C123",
            n_customerName="John Doe",
            n_roomId="R456",
            n_roomNum=101,
            n_hotelName="Grand Hotel",
            n_cost=200.00,
            n_location="New York",
            n_checkIn="2024-05-01",
            n_checkOut="2024-05-10"
        )

    def test_initialization(self):
        self.assertEqual(self.reservation.customerId, "C123")
        self.assertEqual(self.reservation.name, "John Doe")
        self.assertEqual(self.reservation.roomId, "R456")
        self.assertEqual(self.reservation.roomNum, 101)
        self.assertEqual(self.reservation.hotelName, "Grand Hotel")
        self.assertEqual(self.reservation.cost, 200.00)
        self.assertEqual(self.reservation.location, "New York")
        self.assertEqual(self.reservation.checkIn, "2024-05-01")
        self.assertEqual(self.reservation.checkOut, "2024-05-10")

    def test_location_property(self):
        self.assertEqual(self.reservation.location, "New York")

    def test_customerId_property(self):
        self.assertEqual(self.reservation.customerId, "C123")

    def test_name_property(self):
        self.assertEqual(self.reservation.name, "John Doe")

    def test_hotelName_property(self):
        self.assertEqual(self.reservation.hotelName, "Grand Hotel")

    def test_roomNum_property(self):
        self.assertEqual(self.reservation.roomNum, 101)

    def test_roomId_property(self):
        self.assertEqual(self.reservation.roomId, "R456")

    def test_cost_property(self):
        self.assertEqual(self.reservation.cost, 200.00)

    def test_checkIn_property(self):
        self.assertEqual(self.reservation.checkIn, "2024-05-01")

    def test_checkIn_setter(self):
        self.reservation.setCheckIn = "2024-05-02"
        self.assertEqual(self.reservation.checkIn, "2024-05-02")

    def test_checkOut_property(self):
        self.assertEqual(self.reservation.checkOut, "2024-05-10")

    def test_checkOut_setter(self):
        self.reservation.setCheckOut = "2024-05-11"
        self.assertEqual(self.reservation.checkOut, "2024-05-11")

if __name__ == '__main__':
    unittest.main()
