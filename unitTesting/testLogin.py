import unittest
import tkinter as tk
from unittest.mock import MagicMock
from login import Login

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.database = MagicMock()
        self.controller = MagicMock()
        self.login_page = Login(self.root, self.database, self.controller)

    def testReset(self):
        self.login_page.userEmail.insert(0, "test@example.com")
        self.login_page.userPassword.insert(0, "password")
        self.login_page.isUserVar.set(0)
        self.login_page.isAdminVar.set(1)

        self.login_page.reset()

        self.assertEqual(self.login_page.controller.isLoggedIn, False)
        self.assertEqual(self.login_page.controller.isAdmin, False)
        self.assertEqual(self.login_page.isUser, False)
        self.assertEqual(self.login_page.isAdmin, False)
        self.assertEqual(self.login_page.isUserVar.get(), 1)
        self.assertEqual(self.login_page.isAdminVar.get(), 0)
        self.assertEqual(self.login_page.userEmail.get(), "Enter username")
        self.assertEqual(self.login_page.userPassword.get(), "Enter password")

    # Add more test methods for other functionalities of the Login class

if __name__ == '__main__':
    unittest.main()
