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
        self.result = tk.StringVar()

        self.main_frame = tk.Frame(self, width=400, height=400)
        self.main_frame.grid_propagate(0)
        self.main_frame.grid(row=0, column=0)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        
        entry_frame = tk.Frame(self.main_frame)
        entry_frame.grid(row=0, column=0, stick="new")
        entry_frame.grid_rowconfigure(0, weight=1)
        entry_frame.grid_columnconfigure(0, weight=1)
        entry_frame.grid_columnconfigure(1, weight=1)
        
        entry = tk.Entry(entry_frame, textvariable=self.equation, justify='right', font=16)
        entry.grid(row=0, column=0, sticky='ew')

        process_handler = lambda: self.process(None)

        button = tk.Button(entry_frame, text="Calc", command=process_handler)
        button.grid(row=0, column=1, sticky='ew')
        self.bind('<Return>', self.process)


    def process(self, event):
        calc = Calc()
        if calc.parse(self.equation.get(), True) == True:
            reduced, degree_val, result = calc.calcul(self.equation.get(), True)
            self.reduced.set(reduced)
            self.degree.set(degree_val)
            self.result.set(result)

            if degree_val != "None":
                infos_frame = tk.Frame(self.main_frame)
                infos_frame.grid(row=1, column=0, stick="sew")
                infos_frame.grid_columnconfigure(0, weight=1)
                infos_frame.grid_columnconfigure(1, weight=1)
                infos_frame.grid_rowconfigure(0, weight=1)
                infos_frame.grid_rowconfigure(1, weight=1)
                infos_frame.grid_rowconfigure(2, weight=1)
                reduced_label = tk.Label(infos_frame, text="Reduced form : ", font=16)
                reduced_label.grid(row=0, column=0, sticky='w')

                reduced_val = tk.Label(infos_frame, textvariable=self.reduced, font=16)
                reduced_val.grid(row=0, column=1)

                degree_label = tk.Label(infos_frame, text="Degree : ", font=16)
                degree_label.grid(row=1, column=0, sticky='w')

                degree_val = tk.Label(infos_frame, textvariable=self.degree, font=16)
                degree_val.grid(row=1, column=1)

                result_label = tk.Label(infos_frame, text="Result : ", font=16)
                result_label.grid(row=2, column=0, sticky='w')         

                result_val = tk.Label(infos_frame, textvariable=self.result, font=18)
                result_val.grid(row=2, column=1)

            else:
                infos_frame = tk.Frame(self.main_frame)
                infos_frame.grid(row=1, column=0, stick="sew")
                infos_frame.grid_columnconfigure(0, weight=1)
                infos_frame.grid_columnconfigure(1, weight=1)
                infos_frame.grid_rowconfigure(0, weight=1)

                result_label = tk.Label(infos_frame, text="Result : ", font=16)
                result_label.grid(row=0, column=0, sticky='w')         

                result_val = tk.Label(infos_frame, textvariable=self.result, font=18)
                result_val.grid(row=0, column=1)
        else:
            self.reduced.set("")
            self.degree.set("")
            self.result.set("Invalid Input")

            infos_frame = tk.Frame(self.main_frame)
            infos_frame.grid(row=1, column=0, stick="sew")
            infos_frame.grid_columnconfigure(0, weight=1)
            infos_frame.grid_rowconfigure(0, weight=1)

            result_label = tk.Label(infos_frame, text="Result : ", font=16)
            result_label.grid(row=0, column=0, sticky='w')         

            result_val = tk.Label(infos_frame, textvariable=self.result, font=18)
            result_val.grid(row=0, column=1)
