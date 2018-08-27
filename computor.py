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
        calc = Calc()
        gui = False
        for arg in sys.argv[1:]:
            if arg in ("--usage", "--help"):
                print_usage()
                exit(0)
            elif arg == "--gui":
                gui = True
            else:
                equation = calc.parse(arg, gui)
                if equation:
                    if gui:
                        App(equation).mainloop()
                        exit(0)

                    else:
                        calc.calcul(equation, gui)
                        exit(0)
        if gui:
            App("").mainloop()
            exit(0)
    else:
        print_usage()




