# -*- coding: utf-8 -*-

import re

from srcs.ft_calculate import ft_sqrt, ft_power, ft_split_sum

def solve_in_C(discr, tab, variable):
    conj_res = ["", ""]
    conj_res[0] = ""
    conj_res[1] = ""
    return (conj_res)

def ft_discriminator(reduced, variable):
    tab = [0, 0, 0]

    splited = ft_split_sum(reduced.split("=")[0], variable)
    for elem in splited:
        if variable in elem:
            splited_elem = elem.split(variable)
            if len(splited_elem) == 2:
                for i, elem in enumerate(splited_elem):
                    if elem == "-":
                        splited_elem[i] = "-1"
                    elif elem == "+":
                        splited_elem[i] = "+1"
                if splited_elem[1] == "":
                    tab[1] = float(splited_elem[0])
                else:
                    tab[0] = float(splited_elem[0])
        else:
            tab[2] = float(elem)
    b_2 = float(ft_power(tab[1], 2, ""))
    discr = b_2 - (4 * tab[0] * tab[2])
    return (discr, tab)

def ft_find_roots(discr, tab, variable):
    roots = []
    if discr == 0:
        root = -(tab[1] / 2 * tab[0])
        roots.append(str(root))
    else:
        squared_discr = ft_sqrt(discr)
        root1 = (-tab[1] - squared_discr) / (2 * tab[0])
        root2 = (-tab[1] + squared_discr) / (2 * tab[0])
        roots.extend((root1, root2))
    return([str(root) for root in roots])

def ft_solve_deg_1(reduced, variable):
    res = 0
    splited = ft_split_sum(reduced.split("=")[0], variable)
    for elem in reversed(splited):
        if not (variable in elem):
            res -= float(elem)
        else:
            elem = elem.split(variable)[0]
            if re.match('^[+-]+$', elem):
                elem += "1"
            res /= float(elem)
    return (variable + "= " + str(res))

def ft_solve(reduced, variable, deg):
    discr = ""
    result = ""
    if deg == 1:
        result = ft_solve_deg_1(reduced, variable)
    elif deg == 2:
        discr, tab = ft_discriminator(reduced, variable)
        if discr >= 0:
            roots = ft_find_roots(discr, tab, variable)
            if len(roots) == 1:
                result = variable + "= " + roots[0]
            elif len(roots) == 2:
                result = variable + "1= " + roots[0] + " and " + variable + "2= " + roots[1]
            else:
                result = "None"
        else:
            conj_res = solve_in_C(discr, tab, variable)
            result = "None in R, in C: " + variable + "1= " + conj_res[0] + "and " + variable + "2= " + conj_res[1]
    return (discr, result)
