# -*- coding: utf-8 -*-

import re

class Calc(object):

    def reduce(self, equation):
        if "=" in equation:
            #TODO Reduce equation
            reduced = equation
        else:
            reduced = "None"
        return (reduced)
    
    def degree(self, reduced):
        if "=" in reduced:
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
            print("Solving : " + equation)
            print("Reduced form : " + reduced)
            print("Degree : " + degree_val)

    def parse(self, equation):
        if len(equation) > 0 and \
           re.match('^[a-zA-Z0-9+-/*^= ]+$', equation) and \
           not ("i" in equation or "I" in equation):
            if self.check(equation) == True:
                return (True)
        else:
            print("Invalid Value")
            exit(0)

    def check(self, equation):
        variable = None
        for char in equation:
            if re.match('^[a-zA-Z]+$', char):
                if variable == None:
                    variable = char
                elif char != variable:
                    print("Only one variable supported")
                    exit(0)
        return (True)
        
