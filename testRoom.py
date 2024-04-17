import unittest
from room import Room

class TestRoom(unittest.TestCase):
    def test_room_creation(self):
        room = Room(n_hotelName="Hotel A", n_roomNum=101, n_location="City Center", n_cost=100.0)
        self.assertEqual(room.hotelName, "Hotel A")
        self.assertEqual(room.roomNum, 101)
        self.assertEqual(room.location, "City Center")
        self.assertEqual(room.cost, 100.0)

    def test_room_creation_with_defaults(self):
        room = Room()
        self.assertIsNone(room.hotelName)
        self.assertIsNone(room.roomNum)
        self.assertIsNone(room.location)
        self.assertIsNone(room.cost)

    def test_setters(self):
        room = Room()
        room.hotelName = "Hotel B"  # Assigning a value to the property, not calling it
        self.assertEqual(room.hotelName, "Hotel B")

        room.roomNum = 202  # Assigning a value to the property, not calling it
        self.assertEqual(room.roomNum, 202)

        room.location = "Suburb"  # Assigning a value to the property, not calling it
        self.assertEqual(room.location, "Suburb")

        room.cost = 150.0  # Assigning a value to the property, not calling it
        self.assertEqual(room.cost, 150.0)

    def test_genRoomNum(self):
        room_num = Room.genRoomNum(None)
        self.assertTrue(100 <= room_num <= 999)

if __name__ == "__main__":
    unittest.main()