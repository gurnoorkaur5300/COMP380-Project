import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from create import Create

class TestCreate(unittest.TestCase):
    """
    Tests the Create class to ensure proper functionality
    :author: Martin Gallegos Cordero
    :version: 1.0
    """
    
    def setUp(self):
        self.root = tk.Tk()
        self.controller = MagicMock()
        self.database = MagicMock()
        self.create_window = Create(self.controller, self.database, master=self.root)
    
    def tearDown(self):
        self.create_window.destroy()
        self.root.destroy()
    
    def test_passwordMatch(self):
        self.create_window.userPassword.insert(0, "password123")
        self.create_window.userPasswordConfirm.insert(0, "password123")
        self.assertTrue(self.create_window.passwordMatch())

        self.create_window.userPassword.delete(0, tk.END)
        self.create_window.userPasswordConfirm.delete(0, tk.END)
        self.create_window.userPassword.insert(0, "password123")
        self.create_window.userPasswordConfirm.insert(0, "differentPassword")
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.assertFalse(self.create_window.passwordMatch())
            mock_showerror.assert_called_with("Error", "Passwords do not match, Press OK and try again")
    
    def test_validateName(self):
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.assertTrue(self.create_window.validateName("John", "Doe"))
            self.assertFalse(self.create_window.validateName("", "Doe"))
            mock_showerror.assert_called_with("Error", "Please enter both a first and last name")
    
    def test_validateEmail(self):
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.assertTrue(self.create_window.validateEmail("test@example.com"))
            self.assertFalse(self.create_window.validateEmail("invalid-email"))
            mock_showerror.assert_called_with("Error", "Please enter a valid email address")
    
    def test_validatePassword(self):
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.create_window.userPassword.insert(0, "ValidPass123")
            self.create_window.userPasswordConfirm.insert(0, "ValidPass123")
            self.assertTrue(self.create_window.validatePassword("ValidPass123"))
            
            self.assertFalse(self.create_window.validatePassword("short"))
            mock_showerror.assert_called_with("Error", "Password must be at least 8 characters long")

            self.assertFalse(self.create_window.validatePassword("noDigits"))
            mock_showerror.assert_called_with("Error", "Password must contain 1 upper case letter, 1 lower case letter, and 1 digit")
    
    def test_validateDOB(self):
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.assertTrue(self.create_window.validateDOB("01-01-2000"))
            self.assertFalse(self.create_window.validateDOB("01/01/2000"))
            mock_showerror.assert_called_with("Error", "Date of birth should have the format dd-mm-yyyy")
    
    def test_validatePhoneNumber(self):
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.assertTrue(self.create_window.validatePhoneNumber("123-456-7890"))
            self.assertFalse(self.create_window.validatePhoneNumber("1234567890"))
            mock_showerror.assert_called_with("Error", "Phone number should have the format ###-###-####")
    
    def test_getData_success(self):
        self.create_window.userName.insert(0, "John")
        self.create_window.userLastName.insert(0, "Doe")
        self.create_window.userDOB.insert(0, "01-01-2000")
        self.create_window.userEmail.insert(0, "john.doe@example.com")
        self.create_window.userPhone.insert(0, "123-456-7890")
        self.create_window.userPassword.insert(0, "ValidPass123")
        self.create_window.userPasswordConfirm.insert(0, "ValidPass123")
        
        self.create_window.database.insertCustomer.return_value = True
        self.assertTrue(self.create_window.getData())
    
    def test_getData_failure(self):
        self.create_window.userName.insert(0, "")
        self.create_window.userLastName.insert(0, "Doe")
        self.assertFalse(self.create_window.getData())
    
    def test_closeCreate(self):
        with patch.object(self.create_window, 'destroy') as mock_destroy:
            self.create_window.closeCreate()
            mock_destroy.assert_called_once()

if __name__ == '__main__':
    unittest.main()
