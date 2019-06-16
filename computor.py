# -*- coding: utf-8 -*-

from srcs.gui_app import App
from srcs.calc_app import Calc

import sys
from sys import exit

def print_usage():
    print("Usage: python computor [--gui] ['2nd_degree_equation']\n" + \
                        "\t no args: interactive mode"
                        "\t--gui: GUI mode\n" + \
                        "\t--usage, --help, --h: print usage\n")

if __name__ == "__main__":
    calc = Calc()
    gui = False
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg in ("--usage", "--help", "--h"):
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
        equation = input("> ")
        equation = calc.parse(equation, gui)
        if equation:
            calc.calcul(equation, gui)
            exit(0)
