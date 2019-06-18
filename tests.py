# -*- coding: utf-8 -*-

import subprocess
import sys
import progressbar

if sys.platform == "darwin" or sys.platform == "linux":
    new_line = "\n"
else:
    new_line = "\r\n"

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
             
             "3^x=0",
             "3x^4.2=0",

             "x/x=0",
             "0=1x^0",

             "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
             "1 * X^0 + 2 * X^1 + 4 * X^2 = 0 * X^0 + 4 * X^1 + 3 * X^2 + 0 * X^3 + 0 * X^4 + 2 * X^5",

             "1 * X^0 = 2 * X^0",

             "1x^42/x^41.1=0"
             
             ]

    res = 0
    bar = progressbar.ProgressBar()
    for test in bar(tests):
        result = subprocess.run(["python", "computor.py", test], stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8').strip()
        if "Error: " in out or "None" in out or out == usage or len(out) == 0:
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

             "3^4.2",
             "3^-4.2",
             ]

    res = 0
    bar = progressbar.ProgressBar()
    for test in bar(tests):
        test = test.replace(",", ".")
        result = subprocess.run(["python", "computor.py", test], stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8').strip()
        if not("Error :" in out):
            try:
                result = out.split(": ")[1].replace("=0", "")
                real = eval(test.replace("^", "**"))
                if float(result) == float(real):
                    check = "\033[1;32;40m OK"
                    res += 1
                else:
                    check = "\033[1;31;40m NOK, expected : " + str(real)
            except:
                if float(out.split(": ")[1]) == 42 or float(out.split(": ")[1]) == -42:
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
    tests = [["5 * X^0 + 4 * X^1 = 4 * X^0", "4.0X+1.0=0", "X= -0.25"],
             ["2x-2=8", "2.0x-10.0=0", "x= 5.0"],
             ["2x+4x-12=6", "6.0x-18.0=0", "x= 3.0"],
             ["2x^1+4x-12=6", "6.0x-18.0=0", "x= 3.0"],
             ["2x^1+4x-12=12x", "-6.0x-12.0=0", "x= -2.0"],
             ["8x^0+42=-3x^1+2x+42", "x+8.0=0", "x= -8.0"],
             ["4x^2/2x^1+4x-12=12x", "-6.0x-12.0=0", "x= -2.0"],
             ["4x^1/8=4", "0.5x-4.0=0", "x= 8.0"],

             ["4/x+2=5", "-3.0x+4.0=0", "x= 1.3333333333333333"],
             ["4+2=5/x", "6.0x-5.0=0", "x= 0.8333333333333334"],
             ["4/x^-1-3x+2=0", "x+2.0=0", "x= -2.0"],
             ["0=4/x^-1-3x+2", "-1.0x-2.0=0", "x= -2.0"],

             ["x=x/x", "x-1.0=0", "x= 1.0"],
             ["x=x/1x", "x-1.0=0", "x= 1.0"],
             ["x=1x/x", "x-1.0=0", "x= 1.0"],
             ["1x=x/x", "x-1.0=0", "x= 1.0"],

             ["1 * X^0 + 2 * X^1 = - 1 * X^0 + 4 * X^1", "-2.0X+2.0=0", "X= 1.0"],
             ["-1 * X^0 - 2 * X^1 = 1 * X^0 + 2 * X^1", "-4.0X-2.0=0", "X= -0.5"],
             ["1 * X^0 + 2 * X^1 + 3 * X^2 = - 1 * X^0 + 4 * X^1 + 3 * X^2", "-2.0X+2.0=0", "X= 1.0"],

             ["1 * X^0 + 2.5 * X^1 = - 1.561151 * X^0 + 4.000 * X^1", "-1.5X+2.5611509999999997=0", "X= 1.707434"],

             ["1 * X^0 = 1 * X^0", "X = X", "X = R"],

             ["1x^42/x^41=0", "x=0", "x= 0.0"]
         ]

    res = 0
    bar = progressbar.ProgressBar()
    for test in bar(tests):
        result = subprocess.run(["python", "computor.py", test[0]], stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8')
        if not("Error :" in out):
            res_tab = out.split(new_line)
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
    tests = [["5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0", "-9.3X^2+4.0X+4.0=0", "X1= 0.9052204301066356 and X2= -0.47511290322491506"],
             ["2x^2-2=8", "2.0x^2-10.0=0", "x1= -2.2360000000001206 and x2= 2.2360000000001206"],
             ["2x^2+4x-12=6", "2.0x^2+4.0x-18.0=0", "x1= -4.162249999999608 and x2= 2.162249999999607"],
             ["2x^2+4x-12=12x", "2.0x^2-8.0x-12.0=0", "x1= -1.1622499999996072 and x2= 5.162249999999608"],
             ["8x^0+42=-3x^2+2x+42", "3.0x^2-2.0x+8.0=0", "None in R, in C: x1= 0.33 + 1.6i and x2= 0.33 - 1.6i"],
             ["4x^3/2x^1+4x-12=12x", "2.0x^2-8.0x-12.0=0", "x1= -1.1622499999996072 and x2= 5.162249999999608"],
             ["4x^2/8=4", "0.5x^2-4.0=0", "x1= -2.8269999999997997 and x2= 2.8269999999997997"],

             ["4/x-3x+2=0", "-3.0x^2+2.0x+4.0=0", "x1= 1.5351666666667905 and x2= -0.8685000000001238"],
             ["4x^-1-3x+2=0", "-3.0x^2+2.0x+4.0=0", "x1= 1.5351666666667905 and x2= -0.8685000000001238"],

             ["1 * X^0 + 2 * X^1 + 2 * X^2 = - 1 * X^0 + 4 * X^1 + 3 * X^2", "-1.0X^2-2.0X+2.0=0", "X1= 0.7314999999998648 and X2= -2.7314999999998646"],
             ["1 * X^0 + 2 * X^1 + 4 * X^2 = - 1 * X^0 + 4 * X^1 + 3 * X^2", "X^2-2.0X+2.0=0", "None in R, in C: X1= 1.0 + 1.0i and X2= 1.0 - 1.0i"],
             ["2 * X^0 + 2 * X^1 + 4 * X^2 = - 1 * X^0 + 4 * X^1 + 3 * X^2", "X^2-2.0X+3.0=0", "None in R, in C: X1= 1.0 + 1.41i and X2= 1.0 - 1.41i"],
             ["1 * X^0 + 2 * X^1 + 4 * X^2 = 0 * X^0 + 4 * X^1 + 3 * X^2", "X^2-2.0X+1.0=0", "X= 1.0"],
             ["1 * X^0 + 2 * X^1 + 4 * X^2 = 0 * X^0 + 4 * X^1 + 3 * X^2 + 0 * X^3 + 0 * X^4 + 0 * X^5", "X^2-2.0X+1.0=0", "X= 1.0"],
             ["1.8526 * X^0 + 2.989 * X^1 + 2.16 * X^2 = - 1.122241 * X^0 + 4.999 * X^1 + 3.25 * X^2", "-1.0899999999999999X^2-2.01X+2.974841=0", "X1= 0.9697247706420699 and X2= -2.813761467889776"]
         ]

    res = 0
    bar = progressbar.ProgressBar()
    for test in bar(tests):
        result = subprocess.run(["python", "computor.py", test[0]], stdout=subprocess.PIPE)
        out = result.stdout.decode('utf-8')
        if not("Error :" in out):
            res_tab = out.split(new_line)
            reduced = res_tab[1].split(" : ")[1]
            if "Discriminant" in res_tab[2]:
                result = res_tab[3].split(" : ")[1]
            else:
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

#main######################################################
if __name__ == "__main__":
    print("\n\033[1;35;40m*** ComputorV1 Tester ***")
    result = subprocess.run(["python", "computor.py", "--usage"], stdout=subprocess.PIPE)
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
