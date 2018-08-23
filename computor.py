# -*- coding: utf-8 -*-

from srcs.gui_app import App
from srcs.calc_app import Calc

import sys

def print_usage():
    print("Usage: python computor [--gui] <2nd_degree_equation>\n" + \
                        "\t--gui: launch GUI\n" + \
                        "\t--usage: print usage\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        i = 1
        for arg in sys.argv[1:]:
            if arg in ("--usage", "--help"):
                print_usage()
                exit(0)
            elif arg == "--gui":
                if len(sys.argv) >= i + 2:
                    equation = sys.argv[i + 1]
                    calc = Calc(equation)
                    if calc.parse() == True:
                        App(equation).mainloop()
                        exit(0)
                    else:
                        print("Invalid format")
                        exit(0)
                else:
                    App("").mainloop()
                    exit(0)
            else:
                calc = Calc(arg)
                if calc.parse() == True:
                    calc.compute()
                else:
                    print("Invalid format")
                    exit(0)
            i = i + 1
    else:
        print_usage()




