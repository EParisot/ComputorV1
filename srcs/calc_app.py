# -*- coding: utf-8 -*-

from srcs.ft_calculate import ft_calculate
from srcs.ft_solve import ft_solve

import re
from sys import exit

class Calc(object):

    def __init__(self):
        self.sum_list = []
        self.variable = "None"
        self.filters = ["([*/][*/])",           # chained //
                        "([*/][+\-]{2})",       # * or / before - or +
                        "([+-][*/])",           # - or + before * or /
                        "([a-zA-Z][a-zA-Z])",   # letter followed by letter
                        "([a-zA-Z][0-9])",      # letter followed by digit
                        "[+\-*/\^]$",           # operator followed by power
                        "^[*/\^]",              # division followed by power
                        "[a-zA-Z][\^]\d+\.\d+"  # floating point var power
                        ]

    def degree(self, reduced):
        if self.variable != "None":
            if re.search("([a-zA-Z][\^][2-9])", reduced):
                for idx, char in enumerate(reduced):
                    if char == "^":
                        degree_val = int(reduced[idx + 1])
                        break
            elif "^1" in reduced or \
                 (self.variable in reduced and not("^" in reduced)):
                degree_val = 1
            else:
                return ("None")
        else:
            return("None")
        return(str(degree_val))

    def calcul(self, equation, gui):
        # Process reduction / Calc
        reduced, reduced_list = ft_calculate(equation, self.variable, False)
        if len(reduced_list) == 0:
            if gui == False:
                print("Error: Invalid input")
                exit(0)
            else:
                result = "Error: Invalid input"
        # Get degree
        degree_val = self.degree(reduced)
        discr = ""
        # Calculate equation's result
        if degree_val == "None":
            if "=" in reduced and self.variable not in reduced:
                result = "None"
            else:
                result = reduced
            reduced = "None"
        else:
            discr, result = ft_solve(reduced, self.variable, int(degree_val))
        if gui == False:
            if self.variable != "None" and degree_val != "None":
                print("Degree : " + degree_val)
                print("Reduced form : " + reduced)
                if degree_val == "2":
                    if discr > 0:
                        discr = str(discr) + " >0"
                    elif discr < 0:
                        discr = str(discr) + " <0"
                    elif discr == 0:
                        discr = str(discr) + " =0"
                    print("Discriminant : " + discr)
                    print("Result(s) : " + result)
                else:
                    print("Result : " + result)
            else:
                print("Result : " + result)
        return (reduced, degree_val, discr, result)

    def parse(self, equation, gui):
        if len(equation) == 0:
            if gui == False:
                print("Error: Empty input")
                exit(0)
            return (False)
        if re.match("^[a-zA-Z0-9.+\-/*\^= ]+$", equation) and \
           all(not re.search(filt, equation) for filt in self.filters):
            equation = equation.replace(",", ".")
            if self.check(equation, gui) == True:
                return (equation)
            else:
                return (False)
        else:
            if gui == False:
                print("Error: Invalid input")
                exit(0)
            return (False)

    def check(self, equation, gui):
        for char in equation:
            if re.match('^[a-zA-Z]+$', char) and char != "i" and char != "I":
                if self.variable == "None":
                    self.variable = char
                elif char != self.variable:
                    if gui == False:
                        print("Error: Only one variable supported")
                        exit(0)
                    else:
                        return (False)
            elif char == "i" or char == "I":
                if gui == False:
                    print("Error: 'i' or 'I' var forbidden")
                    exit(0)
                else:
                    return (False)
        if re.search("([\^][a-zA-Z])", equation):
            if gui == False:
                print("Error: Variable power not allowed")
                exit(0)
            else:
                return (False)
        var_count = 0
        for char in equation:
            if char == self.variable:
                var_count += 1
        if "=" in equation:
            if self.variable == "None" or \
               (var_count == 1 and self.variable + "^0" in equation):
                if gui == False:
                    print("Error: Missing variable")
                    exit(0)
                else:
                    return (False)
        return (True)

