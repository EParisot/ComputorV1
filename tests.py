# -*- coding: utf-8 -*-

import subprocess

###########################################################
def bastard_tests(usage):
    print("\n\t\033[1;35;40m  -Testing like a Bastard:\n")

    tests = ["",
             "None",
             "null",
             "\t",
             "\n",
             "+",
             "=",

             "3+*4",
             "3-**4",
             "3*--4",
             "3/++4",
             "3/++-4",
             "3*+++4",
             "42**4",
             "42//3",
             "3xx+2",
             "3i+2",
             "3xi-4",
             "42*£",
             "42+µ",

             "42\"",
             "42^",
             "42*",
             "42/",
             "42+",
             "42-",
             "*42",
             "/42",
             "^42",
             ]
    
    for test in tests:
        result = subprocess.run(["python", "computor.py", test], shell=True, stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8').strip()
        if "Error: " in out or out == usage:
            check = "\033[1;32;40m OK"
        else:
            check = "\033[1;31;40m NOK"
        print("\033[1;36;40m " + test + " -> \033[1;33;40m" + out + "\t\t" + check)

###########################################################
def tests_deg_0():
    print("\n\t\033[1;35;40m  -Testing degree 0:\n")
    #remember to use "42" or "-42" as wierd results (to avoid SyntaxError(s)) !
    tests = ["0",
             "0+2",
             " - 4 2 ",
             "+ 42",
             "4.2",
             "4,2",
             
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
             "4.2+37.8",
             
             "2*21",
             "2*-21",
             "-2*21",
             "2*+21",
             "42/2",
             "42/-2",
             "-42/2",

             "3*7+42/2",
             "3*7+42/-2",
             "3*+7+42/2",
             "3*7--42/2",
             "3*-7+42/2",

             "2^0",
             "2^1",
             "2^4",
             "2^-4",
             "2^4/5",
             "2*2^4*5",
             "2*2^-4*5",
             "2/2^-4/5",

             "2x^0-12",
             "4/56.8*-43/12.4--45.678*0.2",
             ]

    for test in tests:
        test = test.replace(",", ".")
        result = subprocess.run(["python", "computor.py", test], stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8').strip()
        if not("Error :" in out):
            try:
                res = out.split(" : ")[1]
                real = eval(test.replace("x^0", "").replace("^", "**"))
                if float(res) == float(real):
                    check = "\033[1;32;40m OK"
                else:
                    check = "\033[1;31;40m NOK, expected : " + str(real)
            except SyntaxError:
                if float(out.split(" : ")[1]) == 42 or float(out.split(" : ")[1]) == -42:
                    check = "\033[1;32;40m OK"
                else:
                    check = "\033[1;31;40m NOK, expected : " + str(real)
        else:
            check = "\033[1;31;40m NOK, expected : " + str(real)
        print("\033[1;36;40m " + test + " -> \033[1;33;40m" + out + "\t\t" + check)

###########################################################
def tests_deg_1():
    print("\n\t\033[1;35;40m  -Testing degree 1:\n")
    #remember to use "42" or "-42" as wierd results (to avoid SyntaxError(s)) !
    tests = [["2x-2=8", "2.0x-10.0=0", "x=5.0"],
             ["2x+4x-12=6", "6.0x-18.0=0", "x=3.0"],
             ["2x^1+4x-12=6", "6.0x-18.0=0", "x=3.0"],
             ["2x^1+4x-12=12x", "-6.0x-12.0=0", "x=2.0"],
             
         ]
    
    for test in tests:
        result = subprocess.run(["python", "computor.py", test[0]], stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8')
        if not("Error :" in out):
            res_tab = out.split("\n")
            reduced = res_tab[1].split(" : ")[1]
            result = res_tab[2].split(" : ")[1]
            if reduced == test[1] and result == test[2]:
                check = "\033[1;32;40m OK"
            else:
                check = "\033[1;31;40m NOK, expected : " + test[1] + " ; " + test[2]
        else:
            check = "\033[1;31;40m NOK, expected : " + test[1] + " ; " + test[2]
        print("\033[1;36;40m " + test[0] + " -> \033[1;33;40m" + out + "\t\t\t\t" + check)


###########################################################
def tests_deg_2():
    pass

#main######################################################
if __name__ == "__main__":
    print("\n\033[1;35;40m*** ComputorV1 Tester ***")
    result = subprocess.run(["python", "computor.py", "--usage"], shell=True, stdout=subprocess.PIPE)
    usage = result.stdout.decode('utf-8').strip()
    bastard_tests(usage)
    tests_deg_0()
    tests_deg_1()
    tests_deg_2()
    exit(0)
