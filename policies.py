import tkinter as tk
from page import Page

class Policies(Page):
    def __init__(self,parent,controller):
        label = tk.Label(self, text="Policies is Alive")
        label.pack()