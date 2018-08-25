# -*- coding: utf-8 -*-

from srcs.ft_reduct import ft_reduct

import re

class Calc(object):

    def __init__(self):
        self.sum_list = []
        self.variable = "None"

    def reduce(self, equation):
        reduced, reduced_list = ft_reduct(equation, self.variable)
        if len(reduced_list) == 0:
            print("Invalid value")
        return(reduced)
    
    def degree(self, reduced):
        if self.variable != "None":
            if "^2" in reduced:
                degree_val = 2
            elif "^1" in reduced or "^0" in reduced or not ("^" in reduced):
                degree_val = 1
            else:
                return("Invalid Degree")
        else:
            return("None")
        return(str(degree_val))
        
    def calcul(self, equation, t_print):
        reduced = self.reduce(equation)
        degree_val = self.degree(reduced)
        #TODO Calculate result
        if t_print == True:
            if self.variable != "None":
                print("Reduced form : " + reduced)
                print("Degree : " + degree_val)
            else:
                print("Result : " + reduced)
        return (reduced, degree_val)

    def parse(self, equation):
        if len(equation) > 0 and \
           re.match('^[a-zA-Z0-9+-/*^= ]+$', equation) and \
           not ("i" in equation or "I" in equation):
            if self.check(equation) == True:
                return (True)
        elif len(equation) > 0:
            print("Invalid Value")
            exit(0)

    def check(self, equation):
        for char in equation:
            if re.match('^[a-zA-Z]+$', char):
                if self.variable == "None":
                    self.variable = char
                elif char != self.variable:
                    print("Only one variable supported")
                    exit(0)
        return (True)
        
