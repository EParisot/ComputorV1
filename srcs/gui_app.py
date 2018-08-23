# -*- coding: utf-8 -*-

import tkinter as tk

class App(tk.Tk):
    def __init__(self, equation):
        tk.Tk.__init__(self)
        self.title("ComputorV1")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.equation = tk.StringVar()
        self.equation.set(equation)
        
        self.entry = tk.Entry(self, textvariable=self.equation)
        self.entry.grid(row=0, column=0, sticky="new")

        self.button = tk.Button(self, text="Calc")
        self.button.grid(row=0, column=1)
        

        
