# -*- coding: utf-8 -*-

import re

def ft_sum_deg_0(members_list):
    res = 0
    for elem in members_list:
        if re.match('^[+-]+$', elem):
            res += 0
        elif re.match('^[0-9+-.]+$', elem):
            res += float(elem)
    s_res = str(res)
    return ("+" + s_res if res > 0 else s_res)

def ft_sum_deg_1_2(members_list, variable, deg):
    res = 0
    for elem in members_list:
        i = 0
        for char in elem:
            if char == variable:                                #Sum-up factors
                if re.match('^[+-]+$', elem[0:i]):
                    res += float(elem[0:i] + "1")
                elif re.match('^[0-9+-.]+$', elem[0:i]):
                    res += float(elem[0:i])
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

def ft_sum(members_list, variable, deg):
    if deg != 0:
        return (ft_sum_deg_1_2(members_list, variable, deg))
    elif deg == 0:                                              #Sum-up digits
        return (ft_sum_deg_0(members_list))
    
def ft_dispatch(member_list, variable):
    deg_0_list = []
    deg_1_list = []
    deg_2_list = []
    ordered_list = []
    for member in member_list:                                  #Dispatch by degree
        if "^2" in member:
            deg_2_list.append(member)
        elif not ("^" in member) and variable in member:
            deg_1_list.append(member)
        elif not ("^" in member) and not (variable in member):
            deg_0_list.append(member)
    deg_2 = ft_sum(deg_2_list, variable, 2)                     #Sum_up by degrees
    deg_1 = ft_sum(deg_1_list, variable, 1)
    deg_0 = ft_sum(deg_0_list, variable, 0)

    if deg_2:
        ordered_list.append(deg_2)
    if deg_1:
        ordered_list.append(deg_1)
    if deg_0:
        ordered_list.append(deg_0)
        
    return(ordered_list)

def ft_prod_deg_0(splited):
    res = 1
    for idx, fact in enumerate(splited):
        if fact[0] == "*" or idx == 0:
            res *= float(fact[1 if idx != 0 else 0:])
        elif fact[0] == "/" or idx == 0:
            res /= float(fact[1 if idx != 0 else 0:])
    return(str(res))

def ft_split_prod(member_list, variable):
    for idx, elem in enumerate(member_list):
        i = 0
        for char in elem:                                       #Count vars
            if char == variable:
                i = i + 1
        if "*" in elem or "/" in elem:
            if i > 0:                                           #TODO make var product
                if i == 1:
                    pass
                else:
                    pass
            else:                                               #TODO make simple product
                j = 0
                splited = []
                for char in elem:
                    if char in "*/" or j == 0:
                        k = j + 1
                        while (k < len(elem) and not(elem[k] in "*/")):
                            k = k + 1
                        splited.append(elem[j:k])
                    j = j + 1
                member_list[idx] = ft_prod_deg_0(splited)
    return(member_list)

def ft_split_sum(member, variable):
    splited = []
    i = 0
    while (i < len(member)):
        if member[i] in "+-" or i == 0:
            j = i + 1
            while (j < len(member) and (not(member[j] in "+-") or member[j - 1] in "/*")):
                j = j + 1                                       #Between each "+" or "-" (not preceded by "/" or "*"):
            signed = member[i:j]                                #Slice a single member
            if not(member[i] in "+-") and i == 0:
                signed = "+" + signed                           #Append "+" if needed
            splited.append(signed)
            i = j - 1
        i = i + 1
    i = 0
    for elem in splited:
        if elem == "-" and \
           i + 1 < len(splited) and \
           splited[i + 1][0] == "-":                       #Turn "--" into "+" for next elem
            splited[i + 1] = splited[i + 1].replace("-", "+")
            splited.pop(i)
        i = i + 1
    splited = ft_split_prod(splited, variable)              #Make member product
    if splited:
        return (splited)
    else:
        return ([])

def ft_calculate(equation, variable):
    reduced = "None"
    equation = equation.replace(" ", "")
    reduced_list = equation.split("=")                          #Split eq in 2
    if len(reduced_list) == 2:
        l_member = reduced_list[0]
        r_member = reduced_list[1]
        reduced_list = ft_split_sum(l_member, variable)             #Split/Prod left members
        r_member = ft_split_sum(r_member, variable)                 #Split/Prod right members
        if reduced_list or r_member:
            if len(reduced_list) > 0:
                i = 0
                for elem in r_member:                           #Rev r_member's sign
                    if elem[0] == "+":
                        r_member[i] = "-" + elem[1:]        
                    elif elem[0] == "-":
                        r_member[i] = "+" + elem[1:]
                    i = i + 1
            reduced_list += r_member                            #Merge members
            reduced_list = ft_dispatch(reduced_list, variable)  #Sum by degree
            if variable != "None":
                reduced = "".join(map(str, reduced_list)) + "=0"
            else:
                reduced = "".join(map(str, reduced_list))
        else:
            return("None", [])
    else:
        reduced_list = ft_split_sum(reduced_list[0], variable)
        reduced_list = ft_dispatch(reduced_list, variable)
        if variable != "None":
            reduced = "".join(map(str, reduced_list)) + "=0"
        else:
            reduced = "".join(map(str, reduced_list))
    if len(reduced) > 0 and reduced[0] == "+":                  #remove first "+"
        reduced = reduced[1:]
    return(reduced, reduced_list)
    
