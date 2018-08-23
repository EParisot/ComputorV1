# -*- coding: utf-8 -*-

class Calc(object):
    
    def __init__(self, equation):
        self.equation = equation
        
    def compute(self):
        #Do the calcul
        print("Solving : " + self.equation)
        exit(0)

    def parse(self):
        if len(self.equation) > 0:
            #Parse input
            return (True)
        else:
            return (False)
        
