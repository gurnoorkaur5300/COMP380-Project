import tkinter as tk
from page import Page

class Policies(Page):
    def __init__(self,parent,controller):
        super().__init__(parent,controller)
        label = tk.Label(self, text="Policies is Alive")
        label.pack()