import tkinter as ttk
from tkinter import *

class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

myApp = App()

myApp.master.geometry("1000x400")

myApp.mainloop()

