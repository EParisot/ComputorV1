# -*- coding: utf-8 -*-

from srcs.calc_app import Calc

import tkinter as tk

class App(tk.Tk):
    def __init__(self, equation):
        tk.Tk.__init__(self)
        self.title("ComputorV1")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.equation = tk.StringVar()
        self.equation.set(equation)
        self.reduced = tk.StringVar()

        self.main_frame = tk.Frame(self, width=400, height=400)
        self.main_frame.grid_propagate(0)
        self.main_frame.grid(row=0, column=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)
        
        self.entry = tk.Entry(self.main_frame, textvariable=self.equation, justify='right', font=16)
        self.entry.grid(row=0, column=0, sticky='e')

        self.button = tk.Button(self.main_frame, text="Calc", command=self.process)
        self.button.grid(row=0, column=1, sticky='w')
        self.bind('<Return>', self.process)

        self.reduced_label = tk.Label(self.main_frame, text="Reduced form : ", font=16)
        self.reduced_label.grid(row=1, column=0, sticky='w')

        self.reduced_val = tk.Label(self.main_frame, textvariable=self.reduced, font=16)
        self.reduced_val.grid(row=1, column=1)

    def process(self, event):
        calc = Calc()
        self.reduced.set(calc.reduce(self.equation.get()))
        calc.calcul(self.equation.get(), False)
