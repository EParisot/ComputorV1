# -*- coding: utf-8 -*-

import subprocess

def bastard_tests(usage):
    print("\n\t\033[1;37;40m  -Testing like a Bastard:\n")

    tests = ["",
             "None",
             "null",
             "\t",
             "\n",
             "+",
             "=",
             ]
    
    for test in tests:
        result = subprocess.run(["python", "computor.py", test], shell=True, stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8').strip()
        if "Error: " in out or out == usage:
            check = "\033[1;32;40m OK"
        else:
            check = "\033[1;31;40m NOK"
        print("\t\033[1;36;40m " + test + " -> \033[1;33;40m" + out + "\t\t\t\t" + check)

def tests_deg_0():
    print("\n\t\033[1;37;40m  -Testing degree 0:\n")
    #remember to use "42" or "-42" as wierd results (to avoid SyntaxError(s)) !
    tests = ["0",
             "0+2",
             " - 4 2 ",
             "+ 42",
             "+42",
             "-42",
             "42",
             "4+2",
             "21+21",
             "4-2",
             "2-2",
             "2-44",
             "2+-44",
             "-44+2",
             "40--2",
             "40++2",
             ]

    for test in tests:
        result = subprocess.run(["python", "computor.py", test], shell=True, stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8').strip()
        try:
            if out == "Result : " + str(eval(test)):
                check = "\033[1;32;40m OK"
            else:
                check = "\033[1;31;40m NOK"
        except SyntaxError:
            if out == "Result : " + "42" or out == "Result : " + "-42":
                check = "\033[1;32;40m OK"
            else:
                check = "\033[1;31;40m NOK"
        print("\t\033[1;36;40m " + test + " -> \033[1;33;40m" + out + "\t\t\t\t" + check)


#main
if __name__ == "__main__":
    print("\n\033[1;35;40m*** ComputorV1 Tester ***")
    result = subprocess.run(["python", "computor.py", "--usage"], shell=True, stdout=subprocess.PIPE)
    usage = result.stdout.decode('utf-8').strip()
    bastard_tests(usage)
    tests_deg_0()
    exit(0)
