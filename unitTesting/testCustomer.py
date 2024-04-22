import unittest
from datetime import datetime
from customer import Customer  

class TestCustomer(unittest.TestCase):

    def testInitWithAllParameters(self):
        dob = "01/01/2000"
        customer = Customer("John Doe", "john@example.com", dob, "1234567890", "hashed_password", [])
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.email, "john@example.com")
        self.assertEqual(customer.dob, dob)
        self.assertEqual(customer.phoneNumber, "1234567890")
        self.assertEqual(customer.hashPass, "hashed_password")
        self.assertEqual(customer.reservations, [])

    def testInitWithDefaultParameters(self):
        customer = Customer()
        self.assertIsNone(customer.name)
        self.assertIsNone(customer.email)
        self.assertIsNone(customer.dob)
        self.assertIsNone(customer.phoneNumber)
        self.assertIsNone(customer.hashPass)
        self.assertEqual(customer.reservations, [])

    def testSetAndGetName(self):
        customer = Customer()
        customer.setName = "Jane Doe"
        self.assertEqual(customer.name, "Jane Doe")

    def testSetAndGetEmail(self):
        customer = Customer()
        customer.setEmail = "jane@example.com"
        self.assertEqual(customer.email, "jane@example.com")

    def testSetAndGetPhoneNumber(self):
        customer = Customer()
        customer.setPhone = "098-765-4321"
        self.assertEqual(customer.phoneNumber, "098-765-4321")

    def testSetAndGetDob(self):
        customer = Customer()
        customer.setDob = "12-31-1999"
        self.assertEqual(customer.dob, "12-31-1999")

    def testAddReservation(self):
        customer = Customer()
        customer.addReservations("Reservation 1")
        self.assertEqual(customer.reservations, ["Reservation 1"])

    def testGetHashPassword(self):
        customer = Customer()
        customer._Customer__hashPass = "hashed_password" 
        self.assertEqual(customer.hashPass, "hashed_password")

if __name__ == '__main__':
    unittest.main()
