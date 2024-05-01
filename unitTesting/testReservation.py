import unittest
from reservation import Reservation

class TestReservation(unittest.TestCase):
    """
    Tests the Reservation class to ensure proper functionality and correct data handling.
    The tests focus on verifying the correct retrieval and updating of reservation details
    such as customer name, room details, and reservation dates.
    
    Author: Gurnoor Kaur
    Version: 1.0
    """

    def setUp(self):
        """
        Set up the test environment before each test.
        Initializes a Reservation instance with predefined data to ensure consistency in testing.
        """
        self.reservation = Reservation(
            n_customerName="John Doe",
            n_roomId=101,
            n_roomNum=1,
            n_hotelName="Example Hotel",
            n_location="Example City",
            n_cost=200,
            n_checkIn="2024-01-01",
            n_checkOut="2024-01-05"
        )

    def test_name(self):
        """
        Tests the name property to verify it returns the correct customer name.
        Asserts the name property matches the expected value set during initialization.
        """
        self.assertEqual(self.reservation.name, "John Doe")

    def test_hotelName(self):
        """
        Tests the hotelName property to confirm it correctly returns the name of the hotel.
        Validates that the property reflects the initialization value.
        """
        self.assertEqual(self.reservation.hotelName, "Example Hotel")

    def test_roomNum(self):
        """
        Tests the roomNum property to ensure it correctly identifies the room number.
        Checks the consistency of room number as set in the reservation's initialization.
        """
        self.assertEqual(self.reservation.roomNum, 1)

    def test_roomId(self):
        """
        Tests the roomId property to ensure it returns the correct identifier for the reserved room.
        Asserts the correctness of the roomId returned against the initialized data.
        """
        self.assertEqual(self.reservation.roomId, 101)

    def test_cost(self):
        """
        Tests the cost property to ensure it reflects the correct cost of the reservation.
        Confirms that the cost is consistent with the value provided at setup.
        """
        self.assertEqual(self.reservation.cost, 200)

    def test_checkIn(self):
        """
        Tests the checkIn property to verify the accuracy of the check-in date.
        Ensures the check-in date matches the expected date set during initialization.
        """
        self.assertEqual(self.reservation.checkIn, "2024-01-01")

    def test_checkOut(self):
        """
        Tests the checkOut property to confirm the correct check-out date is returned.
        Ensures the property is accurate and consistent with the set values.
        """
        self.assertEqual(self.reservation.checkOut, "2024-01-05")

    def test_setCheckIn(self):
        """
        Tests the setter for the check-in date to ensure it correctly updates the date.
        Asserts that the new date is properly set and retrieved through the property.
        """
        self.reservation.setCheckIn = "2024-02-01"
        self.assertEqual(self.reservation.checkIn, "2024-02-01")

    def test_setCheckOut(self):
        """
        Tests the setter for the check-out date to ensure it correctly updates the reservation details.
        Verifies that the new check-out date is accurately reflected in the property.
        """
        self.reservation.setCheckOut = "2024-02-05"
        self.assertEqual(self.reservation.checkOut, "2024-02-05")

if __name__ == '__main__':
    unittest.main()
