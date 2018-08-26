# -*- coding: utf-8 -*-

from srcs.ft_reduct import ft_reduct

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
                return("Invalid Degree")
        else:
            return("None")
        return(str(degree_val))
        
    def calcul(self, equation, gui):
        reduced, reduced_list = ft_reduct(equation, self.variable)      #Process Calc
        if len(reduced_list) == 0:
            if gui == False: 
                print("Invalid input")
                exit(0)
            else:
                result = "Invalid input"
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
                print("Result : " + reduced)
        return (reduced, degree_val, result)



    def parse(self, equation, gui):
        if len(equation) > 0 and \
           re.match('^[a-zA-Z0-9+-/*^= ]+$', equation) and \
           not ("i" in equation or "I" in equation):
            if self.check(equation, gui) == True:
                return (True)
            else:
                return (False)
        elif len(equation) > 0:
            if gui == True:
                print("Invalid input")
            return (False)

    def check(self, equation, gui):
        for char in equation:
            if re.match('^[a-zA-Z]+$', char):
                if self.variable == "None":
                    self.variable = char
                elif char != self.variable:
                    if gui == False:
                        print("Only one variable supported")
                        exit(0)
                    else:
                        return (False)
            if char == "=" and self.variable == "None":
                if gui == False:
                    print("Missing variable")
                    exit(0)
                else:
                    return (False)
        return (True)
        
