import tkinter as tk
from page import Page

class Home(Page):
    def __init__(self,parent,controller):
        label = tk.Label(self, text="Home is Alive")
        label.pack()