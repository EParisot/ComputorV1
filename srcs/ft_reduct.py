# -*- coding: utf-8 -*-

import re

def ft_prod(member_list, variable):
    for elem in member_list:
        i = 0
        for char in elem:
            if char == variable:
                i = i + 1
        if i > 1 and "*" in elem:
            #TODO make product
            pass
        elif i > 1:
            return (None)
    return(member_list)

def ft_split(member, variable):
    reduced_list = []
    i = 0
    while (i < len(member)):
        if member[i] in "+-" or i == 0:
            j = i + 1
            while (j < len(member) and not(member[j] in "+-")):
                j = j + 1
            signed = member[i:j]
            if not(member[i] in "+-") and i == 0:
                signed = "+" + signed
            reduced_list.append(signed)
            i = j - 1
        i = i + 1
    reduced_list = ft_prod(reduced_list, variable)
    if reduced_list:
        return (reduced_list)
    else:
        return ([])

def ft_sum_bis(deg_list, variable, deg):
    res = 0
    if deg != 0:
        for elem in deg_list:
            i = 0
            for char in elem:
                if char == variable:
                    if re.match('^[+-]+$', elem[0:i]):
                        res += int(elem[0:i] + "1")
                    elif re.match('^[0-9+-]+$', elem[0:i]):
                        res += int(elem[0:i])
                i = i + 1
        if deg == 2:
            if res != 0:
                if res == 1:
                    s_res = ""
                else:
                    s_res = str(res)
                return ("+" + s_res + "X^2" if res > 0 else s_res + "X^2")
            else:
                return (None)
        elif deg == 1:
            if res != 0:
                if res == 1:
                    s_res = ""
                else:
                    s_res = str(res)
                return ("+" + s_res + "X" if res > 0 else s_res + "X")
            else:
                return (None)
    elif deg == 0:
        for elem in deg_list:
            res += int(elem)
        if res != 0:
            s_res = str(res)
            return ("+" + s_res if res > 0 else s_res)
        else:
            return (None)
    
def ft_sum(member_list, variable):
    deg_0_list = []
    deg_1_list = []
    deg_2_list = []
    ordered_list = []
    for member in member_list:
        if "^2" in member:
            deg_2_list.append(member)
        elif not ("^" in member) and variable in member:
            deg_1_list.append(member)
        elif not ("^" in member) and not (variable in member):
            deg_0_list.append(member)

    deg_2 = ft_sum_bis(deg_2_list, variable, 2)
    deg_1 = ft_sum_bis(deg_1_list, variable, 1)
    deg_0 = ft_sum_bis(deg_0_list, variable, 0)

    if deg_2:
        ordered_list.append(deg_2)
    if deg_1:
        ordered_list.append(deg_1)
    if deg_0:
        ordered_list.append(deg_0)

    return(ordered_list)

def ft_reduct(equation, variable):
    reduced = "None"
    equation = equation.replace(" ", "")
    reduced_list = equation.split("=")

    if len(reduced_list) == 2:
        l_member = reduced_list[0]
        r_member = reduced_list[1]
        reduced_list = ft_split(l_member, variable)
        r_member = ft_split(r_member, variable)
        if reduced_list or r_member:
            if len(reduced_list) > 0:
                i = 0
                for elem in r_member:
                    if elem[0] == "+":
                        r_member[i] = "-" + elem[1:]
                    elif elem[0] == "-":
                        r_member[i] = "+" + elem[1:]
                    i = i + 1
            reduced_list += r_member
            del l_member
            del r_member

            reduced_list = ft_sum(reduced_list, variable)
            if variable != "None":
                reduced = "".join(map(str, reduced_list)) + "=0"
            else:
                reduced = "".join(map(str, reduced_list))
        else:
            return("None", [])
    else:
        reduced_list = ft_split(reduced_list[0], variable)
        reduced_list = ft_sum(reduced_list, variable)
        if variable != "None":
            reduced = "".join(map(str, reduced_list)) + "=0"
        else:
            reduced = "".join(map(str, reduced_list))

    if reduced[0] == "+":
        reduced = reduced[1:]
    return(reduced, reduced_list)
    
