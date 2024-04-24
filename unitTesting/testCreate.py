import unittest
from unittest.mock import MagicMock
from create import Create

class TestCreate(unittest.TestCase):
    """
    Tests the Create class to ensure proper functionality
    :author: Gregory Calderon
    :version: 1.0
    """
    def setUp(self):
        self.controller = MagicMock()
        self.database = MagicMock()
        self.validatePasswordMock = MagicMock(return_value=True)
        self.passwordMatchMock = MagicMock(return_value=True)
        self.createPage = Create(
            self.controller, self.database,
            validatePassword=self.validatePasswordMock,
            passwordMatch=self.passwordMatchMock
        )
        
    def testValidateNameValid(self):
        result = self.createPage.validateName("John", "Doe")
        self.assertTrue(result)

    def testValidateNameInvalid(self):
        result = self.createPage.validateName("", "Doe")
        self.assertFalse(result)

    def testValidateEmailValid(self):
        result = self.createPage.validateEmail("test@example.com")
        self.assertTrue(result)

    def testValidateEmailInvalid(self):
        result = self.createPage.validateEmail("invalid-email")
        self.assertFalse(result)
        
    def testValidateDOBValid(self):
        result = self.createPage.validateDOB("01-01-2000")
        self.assertTrue(result)

    def testValidateDOBInvalid(self):
        result = self.createPage.validateDOB("01/01/2000")
        self.assertFalse(result)

    def testValidatePhoneNumberValid(self):
        result = self.createPage.validatePhoneNumber("123-456-7890")
        self.assertTrue(result)

    def testValidatePhoneNumberInvalid(self):
        result = self.createPage.validatePhoneNumber("1234567890")
        self.assertFalse(result)

    def testValidatePasswordValid(self):
        result = self.createPage.validatePassword("Password123")
        self.assertTrue(result)
        self.validatePasswordMock.assert_called_once_with("Password123")

    def testValidatePasswordTooShort(self):
        result = self.createPage.validatePassword("short1Ab")
        self.assertTrue(result)
        self.validatePasswordMock.assert_called_once_with("short1Ab")

    def testPasswordMatchValid(self):
        result = self.createPage.passwordMatch("password", "password")
        self.assertTrue(result)
        self.passwordMatchMock.assert_called_once_with("password", "password")

    def testPasswordMatchInvalid(self):
        result = self.createPage.passwordMatch("password", "different")
        self.assertTrue(result)
        self.passwordMatchMock.assert_called_once_with("password", "different")

if __name__ == '__main__':
    unittest.main()
