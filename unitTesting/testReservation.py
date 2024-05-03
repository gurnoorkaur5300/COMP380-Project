import unittest
from reservation import Reservation

class TestReservation(unittest.TestCase):
    """
    Tests the Reservation class to ensure proper functionality
    :author: Arameh Baghdasarian
    :version: 1.0
    """
    def testReservation(self):
        reservation = Reservation(n_customerName="John Smith", n_room=201, n_checkInDate="05-25-2024", n_checkOutDate="05-30-2024", n_paymentID=1001)
        self.assertEqual(reservation.customerName, "John Smith")
        self.assertEqual(reservation.room, 201)
        self.assertEqual(reservation.checkInDate, "05-25-2024")
        self.assertEqual(reservation.checkOutDate, "05-30-2024")
        self.assertEqual(reservation.paymentID, 1001)

    def testReservationCreateDefaults(self):
        reservation = Reservation()
        self.assertIsNone(reservation.customerName)
        self.assertIsNone(reservation.room)
        self.assertIsNone(reservation.checkInDate)
        self.assertIsNone(reservation.checkOutDate)
        self.assertIsNone(reservation.paymentID)

    def testSetters(self):
        reservation = Reservation()
        reservation.customerName = "Code Titan"  # Assigning a value to the property, not calling it
        self.assertEqual(reservation.customerName, "Code Titan")

        reservation.room = 202  # Assigning a value to the property, not calling it
        self.assertEqual(reservation.room, 202)

        reservation.checkInDate = "01-01-2000"  # Assigning a value to the property, not calling it
        self.assertEqual(reservation.checkInDate, "01-01-2000")

        reservation.checkOutDate = "01-02-2000"  # Assigning a value to the property, not calling it
        self.assertEqual(reservation.checkOutDate, "01-02-2000")

if __name__ == "__main__":
    unittest.main()