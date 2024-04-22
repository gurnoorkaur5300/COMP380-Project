import unittest
from administrator import Administrator

class TestAdmin(unittest.TestCase):
    """
    Tests the Administrator class to ensure proper functionality
    :author: Gregory Calderon
    :version: 1.0
    """
    def setUp(self):
        self.admin = Administrator()

    def testSetAndGetAdminName(self):
        self.admin.setAdminName = "John Doe"
        self.assertEqual(self.admin.adminName, "John Doe")

    def testSetAndGetAdminEmail(self):
        self.admin.adminEmail = "john@example.com"
        self.assertEqual(self.admin.adminEmail, "john@example.com")

    def testSetAndGetHashPass(self):
        self.admin.hashPass = "hashedPassword"
        self.assertEqual(self.admin.hashPass, "hashedPassword")