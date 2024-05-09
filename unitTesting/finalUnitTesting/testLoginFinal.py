import unittest
import tkinter as tk
from unittest.mock import MagicMock
from login import Login

class TestLogin(unittest.TestCase):
    """
    Tests the Login class to ensure proper functionality
    :author: Gurnoor Kaur
    :version: 1.0
    """
    def setUp(self):
        self.root = tk.Tk()
        self.database = MagicMock()
        self.controller = MagicMock()

        # Explicitly set mock returns for boolean properties
        self.controller.isLoggedIn = False
        self.controller.isAdmin = False
        self.controller.isUser = False

        self.login_page = Login(self.root, self.database, self.controller)
        self.login_page.pack()  # Ensure the widget is packed for geometry management.

    def testReset(self):
        # Inserting values into entry fields
        self.login_page.userEmail.insert(0, "test@example.com")
        self.login_page.userPassword.insert(0, "password")
        self.login_page.isUserVar.set(0)
        self.login_page.isAdminVar.set(1)

        # Reset the login fields
        self.login_page.reset()

        # Assert the expected outcomes
        self.assertEqual(self.login_page.userEmail.get(), "Enter username")
        self.assertEqual(self.login_page.userPassword.get(), "Enter password")
        self.assertEqual(self.login_page.isUserVar.get(), 1)
        self.assertEqual(self.login_page.isAdminVar.get(), 0)
        self.assertFalse(self.login_page.controller.isLoggedIn)
        self.assertFalse(self.login_page.controller.isAdmin)
        self.assertFalse(self.login_page.controller.isUser)

    # Consider adding more test methods for other functionalities such as validateUserLogin, showCreate, and showUser

if __name__ == '__main__':
    unittest.main()
