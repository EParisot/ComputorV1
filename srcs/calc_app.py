# -*- coding: utf-8 -*-

import re

class Calc(object):

    def __init__(self):
        self.reduced = None
        self.variable = None

    def reduce(self, equation):
        #TODO Reduce eq
        if "=" in equation:
            self.reduced = equation
        else:
            self.reduced = ""
        return (self.reduced)
        
    def calcul(self, equation, t_print):
        self.reduced = self.reduce(equation)
        if t_print == True:
            print("Solving : " + equation)
            print("Reduced form : " + self.reduced)

    def parse(self, equation):
        if len(equation) > 0 and re.match('^[a-zA-Z0-9+-/*^= ]+$', equation):
            if self.check(equation) == True:
                return (True)
        else:
            print("Invalid format")
            exit(0)

    def check(self, equation):
        for char in equation:
            if re.match('^[a-zA-Z]+$', char):
                if self.variable == None:
                    self.variable = char
                elif char != self.variable:
                    print("Only one variable supported")
                    exit(0)
        return (True)
        
