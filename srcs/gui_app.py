# -*- coding: utf-8 -*-

import matplotlib as plt
plt.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
        self.discr = tk.StringVar()

        self.main_frame = tk.Frame(self, padx=20, pady=20)
        self.main_frame.grid(row=0, column=0)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.infos_frame = None
        
        entry_frame = tk.Frame(self.main_frame)
        entry_frame.grid(row=0, column=0, stick="new")
        entry_frame.grid_rowconfigure(0, weight=1)
        entry_frame.grid_columnconfigure(0, weight=1)
        entry_frame.grid_columnconfigure(1, weight=1)
        
        self.entry = tk.Entry(entry_frame, textvariable=self.equation, justify='right', font=16)
        self.entry.grid(row=0, column=0, sticky='ew')
        self.entry.focus_set()

        process_handler = lambda: self.process(None)

        button = tk.Button(entry_frame, text="Calc", font=20, command=process_handler)
        button.grid(row=0, column=1, sticky='ew')
        self.bind('<Return>', self.process)

        buttons_grid = tk.Frame(self.main_frame, padx=10, pady=10)
        buttons_grid.grid(row=1, column=0, stick="new")
        buttons_grid.grid_rowconfigure(0, weight=1)
        buttons_grid.grid_rowconfigure(1, weight=1)
        buttons_grid.grid_rowconfigure(2, weight=1)
        buttons_grid.grid_columnconfigure(0, weight=1)
        buttons_grid.grid_columnconfigure(1, weight=1)
        buttons_grid.grid_columnconfigure(2, weight=1)

        numbers_grid = tk.Frame(buttons_grid, padx=10, pady=10)
        numbers_grid.grid(row=1, column=1)

        numbers_grid.grid_rowconfigure(0, weight=1)
        numbers_grid.grid_rowconfigure(1, weight=1)
        numbers_grid.grid_rowconfigure(2, weight=1)
        numbers_grid.grid_rowconfigure(3, weight=1)
        numbers_grid.grid_columnconfigure(0, weight=1)
        numbers_grid.grid_columnconfigure(1, weight=1)
        numbers_grid.grid_columnconfigure(2, weight=1)
        numbers_grid.grid_columnconfigure(3, weight=1)

        but_1 = tk.Button(numbers_grid, text="1", font=20, width=4, padx=10, pady=10)
        but_1.bind("<Button-1>", self.insert_from_but)
        but_1.grid(row=0, column=0)
        but_2 = tk.Button(numbers_grid, text="2", font=20, width=4, padx=10, pady=10)
        but_2.bind("<Button-1>", self.insert_from_but)
        but_2.grid(row=0, column=1)
        but_3 = tk.Button(numbers_grid, text="3", font=20, width=4, padx=10, pady=10)
        but_3.bind("<Button-1>", self.insert_from_but)
        but_3.grid(row=0, column=2)
        but_4 = tk.Button(numbers_grid, text="4", font=20, width=4, padx=10, pady=10)
        but_4.bind("<Button-1>", self.insert_from_but)
        but_4.grid(row=1, column=0)
        but_5 = tk.Button(numbers_grid, text="5", font=20, width=4, padx=10, pady=10)
        but_5.bind("<Button-1>", self.insert_from_but)
        but_5.grid(row=1, column=1)
        but_6 = tk.Button(numbers_grid, text="6", font=20, width=4, padx=10, pady=10)
        but_6.bind("<Button-1>", self.insert_from_but)
        but_6.grid(row=1, column=2)
        but_7 = tk.Button(numbers_grid, text="7", font=20, width=4, padx=10, pady=10)
        but_7.bind("<Button-1>", self.insert_from_but)
        but_7.grid(row=2, column=0)
        but_8 = tk.Button(numbers_grid, text="8", font=20, width=4, padx=10, pady=10)
        but_8.bind("<Button-1>", self.insert_from_but)
        but_8.grid(row=2, column=1)
        but_9 = tk.Button(numbers_grid, text="9", font=20, width=4, padx=10, pady=10)
        but_9.bind("<Button-1>", self.insert_from_but)
        but_9.grid(row=2, column=2)
        but_dot = tk.Button(numbers_grid, text=".", font=20, width=4, padx=10, pady=10)
        but_dot.bind("<Button-1>", self.insert_from_but)
        but_dot.grid(row=3, column=0) 
        but_0 = tk.Button(numbers_grid, text="0", font=20, width=4, padx=10, pady=10)
        but_0.bind("<Button-1>", self.insert_from_but)
        but_0.grid(row=3, column=1)
        but_power = tk.Button(numbers_grid, text="^", font=20, width=4, padx=10, pady=10)
        but_power.bind("<Button-1>", self.insert_from_but)
        but_power.grid(row=3, column=2)

        operators_grid = tk.Frame(buttons_grid, padx=10, pady=10)
        operators_grid.grid(row=1, column=2)
        
        operators_grid.grid_rowconfigure(0, weight=1)
        operators_grid.grid_rowconfigure(1, weight=1)
        operators_grid.grid_rowconfigure(2, weight=1)
        operators_grid.grid_rowconfigure(3, weight=1)
        operators_grid.grid_columnconfigure(0, weight=1)

        but_plus = tk.Button(operators_grid, text="+", font=20, width=4, padx=10, pady=10)
        but_plus.bind("<Button-1>", self.insert_from_but)
        but_plus.grid(row=0, column=0) 
        but_min = tk.Button(operators_grid, text="-", font=20, width=4, padx=10, pady=10)
        but_min.bind("<Button-1>", self.insert_from_but)
        but_min.grid(row=1, column=0)
        but_mult = tk.Button(operators_grid, text="*", font=20, width=4, padx=10, pady=10)
        but_mult.bind("<Button-1>", self.insert_from_but)
        but_mult.grid(row=2, column=0) 
        but_div = tk.Button(operators_grid, text="/", font=20, width=4, padx=10, pady=10)
        but_div.bind("<Button-1>", self.insert_from_but)
        but_div.grid(row=3, column=0)

        variables_grid = tk.Frame(buttons_grid, padx=10, pady=10)
        variables_grid.grid(row=1, column=0)
        
        variables_grid.grid_rowconfigure(0, weight=1)
        variables_grid.grid_rowconfigure(1, weight=1)
        variables_grid.grid_rowconfigure(2, weight=1)
        variables_grid.grid_rowconfigure(3, weight=1)
        variables_grid.grid_columnconfigure(0, weight=1)

        but_egal = tk.Button(variables_grid, text="=", font=20, width=4, padx=10, pady=10)
        but_egal.bind("<Button-1>", self.insert_from_but)
        but_egal.grid(row=0, column=0)
        but_x = tk.Button(variables_grid, text="x", font=20, width=4, padx=10, pady=10)
        but_x.bind("<Button-1>", self.insert_from_but)
        but_x.grid(row=1, column=0) 
        but_y = tk.Button(variables_grid, text="y", font=20, width=4, padx=10, pady=10)
        but_y.bind("<Button-1>", self.insert_from_but)
        but_y.grid(row=2, column=0)
        but_z = tk.Button(variables_grid, text="z", font=20, width=4, padx=10, pady=10)
        but_z.bind("<Button-1>", self.insert_from_but)
        but_z.grid(row=3, column=0) 

        utils_grid = tk.Frame(buttons_grid, padx=10, pady=10)
        utils_grid.grid(row=0, column=1, columnspan=2, sticky="e")
        
        utils_grid.grid_columnconfigure(0, weight=1)
        utils_grid.grid_columnconfigure(1, weight=1)
        utils_grid.grid_rowconfigure(0, weight=1)

        but_del = tk.Button(utils_grid, text="del", font=20, width=4, padx=10, pady=10, command=self.delete)
        but_del.grid(row=0, column=1) 
        but_clear = tk.Button(utils_grid, text="C", font=20, width=4, padx=10, pady=10, command=self.clear)
        but_clear.grid(row=0, column=2)

    def delete(self):
        self.entry.delete(len(self.entry.get())-1, "end")

    def clear(self):
        self.entry.delete(0, "end")
        if self.infos_frame:
            self.infos_frame.destroy()

    def insert_from_but(self, event):
        self.entry.insert("end", event.widget['text'])

    def show_graph(self, reduced, calc):
        fig = Figure(figsize=(5, 5), dpi=100)
        a = fig.add_subplot(111)

        def f(val):
            variable = calc.variable
            idx = 0
            reduced_left = reduced.split("=")[0]
            for i, char in enumerate(reduced_left):
                if char == variable:
                    idx = i
            if idx != 0 and reduced_left[i:i+1].isdigit():
                var_value = "*" + str(val)
            else:
                var_value = str(val)
            function = reduced_left.replace(variable, var_value)
            print(function)
            return calc.calcul(function, True)
        
        x = [elem for elem in range(-9, 10)]
        y = [float(f(elem)[-1]) for elem in x]
        a.plot(x, y)

        a.axhline(0, color='black')
        a.axvline(0, color='black')
        
        canvas = FigureCanvasTkAgg(fig, self.main_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(column=1,row=1)
        
    def process(self, event):
        calc = Calc()
        if calc.parse(self.equation.get(), True):
            reduced, degree_val, discr, result = calc.calcul(self.equation.get(), True)
            self.reduced.set(reduced)
            self.degree.set(degree_val)
            self.result.set(result)
            self.discr.set(discr)

            if degree_val != "None":

                if self.infos_frame:
                    self.infos_frame.destroy()
                
                self.infos_frame = tk.Frame(self.main_frame)
                self.infos_frame.grid(row=2, column=0, stick="sew")
                self.infos_frame.grid_columnconfigure(0, weight=1)
                self.infos_frame.grid_columnconfigure(1, weight=1)
                self.infos_frame.grid_rowconfigure(0, weight=1)
                self.infos_frame.grid_rowconfigure(1, weight=1)
                self.infos_frame.grid_rowconfigure(2, weight=1)
                self.infos_frame.grid_rowconfigure(3, weight=1)
                reduced_label = tk.Label(self.infos_frame, text="Reduced form : ", font=16)
                reduced_label.grid(row=0, column=0, sticky='w')

                reduced_val = tk.Label(self.infos_frame, textvariable=self.reduced, font=16)
                reduced_val.grid(row=0, column=1)

                degree_label = tk.Label(self.infos_frame, text="Degree : ", font=16)
                degree_label.grid(row=1, column=0, sticky='w')

                degree_val = tk.Label(self.infos_frame, textvariable=self.degree, font=16)
                degree_val.grid(row=1, column=1)

                if self.discr.get() != "":
                    discr_label = tk.Label(self.infos_frame, text="Discriminator : ", font=16)
                    discr_label.grid(row=2, column=0, sticky='w')         

                    discr_val = tk.Label(self.infos_frame, textvariable=self.discr, font=18)
                    discr_val.grid(row=2, column=1)

                result_label = tk.Label(self.infos_frame, text="Result : ", font=16)
                result_label.grid(row=3, column=0, sticky='w')         

                result_val = tk.Label(self.infos_frame, textvariable=self.result, font=18)
                result_val.grid(row=3, column=1)

                if self.result != None:
                    self.show_graph(self.reduced.get(), calc)

            else:
                if self.infos_frame:
                    self.infos_frame.destroy()
                         
                self.infos_frame = tk.Frame(self.main_frame)
                self.infos_frame.grid(row=2, column=0, stick="sew")
                self.infos_frame.grid_columnconfigure(0, weight=1)
                self.infos_frame.grid_columnconfigure(1, weight=1)
                self.infos_frame.grid_rowconfigure(0, weight=1)

                result_label = tk.Label(self.infos_frame, text="Result : ", font=16)
                result_label.grid(row=0, column=0, sticky='w')         

                result_val = tk.Label(self.infos_frame, textvariable=self.result, font=18)
                result_val.grid(row=0, column=1)
        else:
            self.reduced.set("")
            self.degree.set("")
            self.result.set("Invalid Input")

            if self.infos_frame:
                self.infos_frame.destroy()

            self.infos_frame = tk.Frame(self.main_frame)
            self.infos_frame.grid(row=2, column=0, stick="sew")
            self.infos_frame.grid_columnconfigure(0, weight=1)
            self.infos_frame.grid_rowconfigure(0, weight=1)

            result_label = tk.Label(self.infos_frame, text="Result : ", font=16)
            result_label.grid(row=0, column=0, sticky='w')         

            result_val = tk.Label(self.infos_frame, textvariable=self.result, font=18)
            result_val.grid(row=0, column=1)
