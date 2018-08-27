# -*- coding: utf-8 -*-

from srcs.ft_calculate import ft_calculate

import re

class Calc(object):

    def __init__(self):
        self.sum_list = []
        self.variable = "None"
    
    def degree(self, reduced):
        if self.variable != "None":
            if "^2" in reduced:
                degree_val = 2
            elif "^1" in reduced or "^0" in reduced or not ("^" in reduced):
                degree_val = 1
            else:
                return("Error: Invalid Degree")
        else:
            return("None")
        return(str(degree_val))
        
    def calcul(self, equation, gui):
        reduced, reduced_list = ft_calculate(equation, self.variable)      #Process Calc
        if len(reduced_list) == 0:
            if gui == False: 
                print("Error: Invalid input")
                exit(0)
            else:
                result = "Error: Invalid input"
        degree_val = self.degree(reduced)
        if degree_val == "None":
            result = reduced
            reduced = "None"
        else:
            #TODO Calculate result
            result = ""
        if gui == False:
            if self.variable != "None":
                print("Reduced form : " + reduced)
                print("Degree : " + degree_val)
            else:
                print("Result : " + result)
        return (reduced, degree_val, result)

    def parse(self, equation, gui):
        if len(equation) > 0 and \
           re.match("^[a-zA-Z0-9.+\-/*\^= ]+$", equation) and \
           any(char.isdigit() for char in equation) and \
           not re.search("([*/][+\-]{2})", equation) and \
           not re.search("([*/][*/])", equation) and \
           not re.search("([a-zA-Z][a-zA-Z])", equation) and\
           not re.search("[+\-*/\^]$", equation):
            equation = equation.replace(",", ".")
            if self.check(equation, gui) == True:
                return (equation)
            else:
                return (False)
        else:
            if gui == False:
                print("Error: Invalid input")
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
            if char == "=" and self.variable == "None":
                if gui == False:
                    print("Error: Missing variable")
                    exit(0)
                else:
                    return (False)
        return (True)
        
