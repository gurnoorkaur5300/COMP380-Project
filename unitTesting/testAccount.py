import unittest
from unittest.mock import MagicMock
from account import Account
from customer import Customer

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.controller = MagicMock()
        self.database = MagicMock()
        self.customer = Customer("John Doe", "john@example.com", "01-01-2000", "123-456-7890","Passowrd", ["3agjek"])
        self.customer.addReservations("Reservation 1")
        self.customer.addReservations("Reservation 2")
        self.accountPage = Account(None, self.database, self.controller, self.customer)

    def testSetCustomer(self):
        customer = Customer("Alice Smith", "alice@example.com", "02/02/1990", "987-654-3210")
        self.accountPage.setCustomer(customer)
        self.assertEqual(self.accountPage.customer, customer)

    def testClearLoginEntryBoxes(self):
        self.controller.loginPage.reset = MagicMock()
        self.accountPage.clearLoginEntryBoxes()
        self.controller.loginPage.reset.assert_called_once()

if __name__ == '__main__':
    unittest.main()
