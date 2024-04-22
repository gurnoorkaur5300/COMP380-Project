import unittest
from unittest.mock import MagicMock
from account import Account
from customer import Customer

class TestAccount(unittest.TestCase):
    """
    Tests the Account class to ensure proper functionality
    :author: Gregory Calderon
    :version: 1.0
    """

    def setUp(self):
        """
        Set up the test environment. Create mock objects for controller and databse. Create a mock customer object with sample data. Initialize the Account page with it.
        
        Mocks:
        - controler: A MagicMock object simulating the controller for page navigation.
        - database: A MagicMock object simulating the database that contains customer information.
        
        Sample Customer Data: 
        - Name: John Doe
        - Email: john@example.com
        - Date of Birth: 01-01-2000
        - Phone Number: 123-456-7890
        - Password: Password
        - Reservations: A list containing two sample reservations ("Reservation 1", "Reservation 2").
        
        Initialization:
        - Initialize a Customer object with the sample data.
        - Add two sample reservations to the customer object.
        - Initialize an Account page object with the mocked database, controller, and customer.
        """
        self.controller = MagicMock()
        self.database = MagicMock()
        self.customer = Customer("John Doe", "john@example.com", "01-01-2000", "123-456-7890","Passowrd", ["3agjek"])
        self.customer.addReservations("Reservation 1")
        self.customer.addReservations("Reservation 2")
        self.accountPage = Account(None, self.database, self.controller, self.customer)

    def testSetCustomer(self):
        """
        Tests addition of customer to database. Creates a Customer class and then adds the customer to the account page. Checks if customer on account page matches customer created
        """
        customer = Customer("Alice Smith", "alice@example.com", "02-02-1990", "987-654-3210")
        self.accountPage.setCustomer(customer)
        self.assertEqual(self.accountPage.customer, customer)

    def testClearLoginEntryBoxes(self):
        """
        Tests clearing of login entry boxes.
        """
        self.controller.loginPage.reset = MagicMock()
        self.accountPage.clearLoginEntryBoxes()
        self.controller.loginPage.reset.assert_called_once()

if __name__ == '__main__':
    unittest.main()
