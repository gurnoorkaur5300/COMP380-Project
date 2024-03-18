import tkinter as tk
from page import Page

class Account(Page):
    def __init__(self,parent,controller):
        Page.__init__(self,parent,controller)
        label = tk.Label(self, text="Account is Alive")
        label.pack()