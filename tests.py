# -*- coding: utf-8 -*-

import subprocess
import sys

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
             "42x*42y",
             "42\"",
             "42*",
             "42/",
             "42+",
             "42-",
             "*42",
             "/42",
             "x^42",
             
             "4x^0/8=4",
             "3+(4*(3*4)))",
             "(3+4)(3*4)",
             ]

    res = 0
    for test in tests:
        result = subprocess.run(["python", "computor.py", test], shell=True, stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8').strip()
        if "Error: " in out or out == usage:
            check = "\033[1;32;40m OK"
            res += 1
        else:
            check = "\033[1;31;40m NOK"
        print("\033[1;36;40m " + test + " -> \033[1;33;40m" + out + "\t\t" + check)
    return(res, len(tests))

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

             "2x^0+40",
             "42x^4/1x^4",
             "4/56.8*-43/12.4--45.678*0.2",

             "3+(4*(3*4))",
             "(3+4)*(3*4)",
             "(3+(4+12))*(3*(4 + 12))",

             ]

    res = 0
    for test in tests:
        test = test.replace(",", ".")
        result = subprocess.run(["python", "computor.py", test], stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8').strip()
        if not("Error :" in out):
            try:
                result = out.split(" : ")[1].replace("=0", "")
                real = eval(test.replace("^", "**"))
                if float(result) == float(real):
                    check = "\033[1;32;40m OK"
                    res += 1
                else:
                    check = "\033[1;31;40m NOK, expected : " + str(real)
            except:
                if float(out.split(" : ")[1]) == 42 or float(out.split(" : ")[1]) == -42:
                    check = "\033[1;32;40m OK"
                    res += 1
                else:
                    check = "\033[1;31;40m NOK, expected : " + str(real)
        else:
            check = "\033[1;31;40m NOK, expected : " + str(real)
        print("\033[1;36;40m " + test + " -> \033[1;33;40m" + out + "\t\t" + check)
    return (res, len(tests))

###########################################################
def tests_deg_1():
    print("\n\t\033[1;35;40m  -Testing degree 1:\n")
    #remember to use "42" or "-42" as wierd results (to avoid SyntaxError(s)) !
    tests = [["2x-2=8", "2.0x-10.0=0", "x= 5.0"],
             ["2x+4x-12=6", "6.0x-18.0=0", "x= 3.0"],
             ["2x^1+4x-12=6", "6.0x-18.0=0", "x= 3.0"],
             ["2x^1+4x-12=12x", "-6.0x-12.0=0", "x= -2.0"],
             ["8x^0+42=-3x^1+2x+42", "x+8.0=0", "x= -8.0"],
             ["4x^2/2x^1+4x-12=12x", "-6.0x-12.0=0", "x= -2.0"],
             ["4x^1/8=4", "0.5x-4.0=0", "x= 8.0"],
             ["3+(4*(3*4x))", "48.0x+3.0=0", "x= -0.0625"],

             ["((12x+4)*(3*4))", "144.0x+48.0=0", "x= -0.3333333333333333"],
             ["(3*4)*(12x+4)", "144.0x+48.0=0", "x= -0.3333333333333333"],
             ["(12x+4)*(3*4)", "144.0x+48.0=0", "x= -0.3333333333333333"],
             ["(3+4x^1)*(3*4)", "48.0x+36.0=0", "x= -0.75"],
             ["((3*4)*(12x+4))", "144.0x+48.0=0", "x= -0.3333333333333333"], # error
             
             ["(3+(4+12x))*(3*(4 + 12))", "576.0x+336.0=0", "x= -0.5833333333333334"],
         ]

    res = 0
    for test in tests:
        result = subprocess.run(["python", "computor.py", test[0]], stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8')
        if not("Error :" in out):
            res_tab = out.split("\r\n")
            reduced = res_tab[1].split(" : ")[1]
            result = res_tab[2].split(" : ")[1]

            if reduced == test[1] and result == test[2]:
                check = "\033[1;32;40m OK"
                res += 1
            else:
                check = "\033[1;31;40m NOK, expected : " + test[1] + " ; " + test[2]
        else:
            check = "\033[1;31;40m NOK, expected : " + test[1] + " ; " + test[2]
        print("\033[1;36;40m " + test[0] + " -> \033[1;33;40m" + out + "\t\t\t\t" + check)
    return(res, len(tests))

###########################################################
def tests_deg_2():
    print("\n\t\033[1;35;40m  -Testing degree 2:\n")
    #remember to use "42" or "-42" as wierd results (to avoid SyntaxError(s)) !
    tests = [["2x^2-2=8", "2.0x^2-10.0=0", ""],
             ["2x^2+4x-12=6", "2.0x^2+4.0x-18.0=0", ""],
             ["2x^2+4x-12=6", "2.0x^2+4.0x-18.0=0", ""],
             ["2x^2+4x-12=12x", "2.0x^2-8.0x-12.0=0", ""],
             ["8x^0+42=-3x^2+2x+42", "3.0x^2-2.0x+8.0=0", ""],
             ["4x^3/2x^1+4x-12=12x", "2.0x^2-8.0x-12.0=0", ""],
             ["4x^2/8=4", "0.5x^2-4.0=0", ""],
         ]

    res = 0
    for test in tests:
        result = subprocess.run(["python", "computor.py", test[0]], stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8')
        if not("Error :" in out):
            res_tab = out.split("\r\n")
            reduced = res_tab[1].split(" : ")[1]
            result = res_tab[3].split(" : ")[1]

            if reduced == test[1]:# and result == test[3]:
                check = "\033[1;32;40m OK"
                res += 1
            else:
                check = "\033[1;31;40m NOK, expected : " + test[1] + " ; " + test[3]
        else:
            check = "\033[1;31;40m NOK, expected : " + test[1] + " ; " + test[3]
        print("\033[1;36;40m " + test[0] + " -> \033[1;33;40m" + out + "\t\t\t\t" + check)
    return(res, len(tests))

#main######################################################
if __name__ == "__main__":
    print("\n\033[1;35;40m*** ComputorV1 Tester ***")
    result = subprocess.run(["python", "computor.py", "--usage"], shell=True, stdout=subprocess.PIPE)
    usage = result.stdout.decode('utf-8').strip()
    res = 0
    total = 0
    if len(sys.argv) > 1:
        if "0" in sys.argv[1] or "-A" in sys.argv[1]:
            res_t, total_t = bastard_tests(usage)
            res += res_t
            total += total_t
            res_t, total_t = tests_deg_0()
            res += res_t
            total += total_t
        if "1" in sys.argv[1] or "-A" in sys.argv[1]:
            res_t, total_t = tests_deg_1()
            res += res_t
            total += total_t
        if "2" in sys.argv[1] or "-A" in sys.argv[1]:
            res_t, total_t = tests_deg_2()
            res += res_t
            total += total_t
        print("\n\033[1;35;40m \t\tTotal Result : " + str(res) + "/" + str(total) + ("\033[1;32;40m \tGood Job !!" if res == total else "\033[1;31;40m \tTry again..."))
    else:
        print("usage: tests.py [-A] or [0][1][2]")
    exit(0)
