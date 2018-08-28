# -*- coding: utf-8 -*-

from srcs.ft_calculate import ft_calculate

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
        reduced, reduced_list = ft_calculate(equation, self.variable)      #Process reduction / Calc
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
            #TODO Calculate equation's result
            result = ""
        if gui == False:
            if self.variable != "None" and degree_val != "None":
                print("Degree : " + degree_val)
                print("Reduced form : " + reduced)
                print("Result : " + result)
            else:
                print("Result : " + result)
        return (reduced, degree_val, result)

    def parse(self, equation, gui):
        if len(equation) > 0 and \
           re.match("^[a-zA-Z0-9.+\-/*\^= ]+$", equation) and \
           any(char.isdigit() for char in equation) and \
           not re.search("([*/][+\-]{2})", equation) and \
           not re.search("([*/][*/])", equation) and \
           not re.search("([+-][*/])", equation) and \
           not re.search("([a-zA-Z][a-zA-Z])", equation) and\
           not re.search("[+\-*/\^]$", equation) and \
           not re.search("^[*/\^]", equation):
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
            elif re.search("([a-zA-Z][\^][5-9])", equation):
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
            if char == "=" and self.variable == "None":
                if gui == False:
                    print("Error: Missing variable")
                    exit(0)
                else:
                    return (False)
        return (True)
        
