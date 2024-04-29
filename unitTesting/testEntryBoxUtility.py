import unittest
import tkinter as tk
from entryBoxUtility import EntryBoxUtility

class TestEntryBoxUtility(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    def test_clearEntries(self):
        entry = tk.Entry(self.root)
        entry.defaultText = "Enter text here"
        entry.insert(0, "Enter text here")
        entry.bind("<FocusIn>", EntryBoxUtility.clearEntries)
        entry.event_generate("<FocusIn>")
        self.assertEqual(entry.get(), "")

    def test_handlePasswordFocusIn(self):
        entry = tk.Entry(self.root, show="")
        entry.defaultText = "Enter password"
        entry.insert(0, "Enter password")
        entry.bind("<FocusIn>", EntryBoxUtility.handlePasswordFocusIn)
        entry.event_generate("<FocusIn>")
        self.assertEqual(entry.get(), "")
        self.assertEqual(entry["show"], "*")

    def test_handleEntryFocusOut(self):
        entry = tk.Entry(self.root)
        entry.defaultText = "Enter text here"
        entry.insert(0, "")
        entry.bind("<FocusOut>", EntryBoxUtility.handleEntryFocusOut)
        entry.event_generate("<FocusOut>")
        self.assertEqual(entry.get(), "Enter text here")

    def test_handleEntryFocusIn(self):
        entry = tk.Entry(self.root)
        entry.defaultText = "Enter text here"
        entry.insert(0, "Enter text here")
        entry.bind("<FocusIn>", EntryBoxUtility.handleEntryFocusIn)
        entry.event_generate("<FocusIn>")
        self.assertEqual(entry.get(), "")
        self.assertEqual(entry["show"], "")

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
