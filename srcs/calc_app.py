# -*- coding: utf-8 -*-

from srcs.ft_calculate import ft_calculate
from srcs.ft_solve import ft_solve

import re

class Calc(object):

    def __init__(self):
        self.sum_list = []
        self.variable = "None"
    
    def degree(self, reduced):
        if self.variable != "None":
            if re.search("([a-zA-Z][\^][2-4])", reduced):
                for idx, char in enumerate(reduced):
                    if char == "^":   
                        degree_val = int(reduced[idx + 1])
            elif "^1" in reduced or (self.variable in reduced and not("^" in reduced)):
                degree_val = 1
            else:
                return ("None")
        else:
            return("None")
        return(str(degree_val))
        
    def calcul(self, equation, gui):
        reduced, reduced_list = ft_calculate(equation, self.variable, False)        #Process reduction / Calc
        if len(reduced_list) == 0:
            if gui == False:
                print("Error: Invalid input")
                exit(0)
            else:
                result = "Error: Invalid input"
        degree_val = self.degree(reduced)
        discr = ""
        if degree_val == "None":
            result = reduced
            reduced = "None"
        else:
            discr, result = ft_solve(reduced, self.variable, int(degree_val))       #Calculate equation's result
        if gui == False:
            if self.variable != "None" and degree_val != "None":
                print("Degree : " + degree_val)
                print("Reduced form : " + reduced)
                if degree_val == "2":
                    if discr > 0:
                        discr = ">0"
                    elif discr < 0:
                        discr = "<0"
                    elif discr == 0:
                        discr = "=0"
                    print("Discriminator : " + discr)
                    print("Result(s) : " + result)
                else:
                    print("Result : " + result)
            else:
                print("Result : " + result)
        return (reduced, degree_val, discr, result)

    def parse(self, equation, gui):
        if len(equation) > 0 and \
           re.match("^[a-zA-Z0-9.+\-/*\^= \(\)]+$", equation) and \
           any(char.isdigit() for char in equation) and \
           not re.search("([*/][+\-]{2})", equation) and \
           not re.search("([*/][*/])", equation) and \
           not re.search("([+-][*/])", equation) and \
           not re.search("([a-zA-Z][a-zA-Z])", equation) and\
           not re.search("([a-zA-Z][0-9])", equation) and\
           not re.search("[+\-*/\^]$", equation) and \
           not re.search("^[*/\^]", equation) and \
           not re.search("([\)][\(])", equation) and \
           not re.search("([\)][0-9a-zA-Z])", equation) and \
           not re.search("([0-9a-zA-Z][\(])", equation) and \
           not re.search("[\^][0-9][.]", equation):
            equation = equation.replace(",", ".")
            if self.check(equation, gui) == True:
                return (equation)
            else:
                return (False)
        else:
            if gui == False:
                if re.search("[\^][0-9][.]", equation):
                    print("Error: Fractional powers not supported (yet)")
                else:
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
            elif re.search("([a-zA-Z][\^][5-9])", equation) or re.search("([a-zA-Z][\^][0-9]{2})", equation):
                if gui == False:
                    print("Error: Too high degree")
                    exit(0)
                else:
                    return (False)
                return (False)
            elif char == "i" or char == "I":
                if gui == False:
                    print("Error: 'i' or 'I' var forbidden")
                    exit(0)
                else:
                    return (False)
        var_count = 0
        for char in equation:
            if char == self.variable:
                var_count += 1
        if "=" in equation:
            if self.variable == "None" or (var_count == 1 and self.variable + "^0" in equation):
                if gui == False:
                    print("Error: Missing variable")
                    exit(0)
                else:
                    return (False)
        o_par_count = 0
        c_par_count = 0
        for char in equation:
            if char == "(":
                o_par_count += 1
            elif char == ")":
                c_par_count += 1
        if o_par_count != c_par_count:
            if gui == False:
                print("Error: Incorrect '()'")
                exit(0)
            else:
                return (False)
        return (True)
        
