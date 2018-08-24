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
        self.degree = tk.StringVar()

        main_frame = tk.Frame(self, width=400, height=400)
        main_frame.grid_propagate(0)
        main_frame.grid(row=0, column=0)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        
        entry = tk.Entry(main_frame, textvariable=self.equation, justify='right', font=16)
        entry.grid(row=0, column=0, sticky='e')

        process_handler = lambda: self.process(None)

        button = tk.Button(main_frame, text="Calc", command=process_handler)
        button.grid(row=0, column=1, sticky='w')
        self.bind('<Return>', self.process)

        reduced_label = tk.Label(main_frame, text="Reduced form : ", font=16)
        reduced_label.grid(row=1, column=0, sticky='w')

        reduced_val = tk.Label(main_frame, textvariable=self.reduced, font=16)
        reduced_val.grid(row=1, column=1)

        degree_label = tk.Label(main_frame, text="Degree : ", font=16)
        degree_label.grid(row=2, column=0, sticky='w')

        degree_val = tk.Label(main_frame, textvariable=self.degree, font=16)
        degree_val.grid(row=2, column=1)

    def process(self, event):
        calc = Calc()
        self.reduced.set(calc.reduce(self.equation.get()))
        self.degree.set(calc.degree(self.reduced.get()))
        calc.calcul(self.equation.get(), False)
