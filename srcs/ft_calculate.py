# -*- coding: utf-8 -*-

import re

def ft_sum_deg_0(members_list, variable):
    res = 0
    for elem in members_list:    
        elem = elem.replace(variable + "^0", "")
        if re.match('^[+-]+$', elem):
            res += 0
        elif re.match('^[0-9+-.]+$', elem):
            res += float(elem)
    s_res = str(res)
    if res != 0:
        return ("+" + s_res if res > 0 else s_res)
    else:
        return (None)

def ft_sum_deg(members_list, variable, deg):
    res = 0
    for elem in members_list:
        i = 0
        for char in elem:
            if char == variable:                                                #Sum-up factors
                if re.match('^[+-]+$', elem[0:i]):
                    res += float(elem[0:i] + "1")
                elif re.match('^[0-9+-.]+$', elem[0:i]):
                    res += float(elem[0:i])
            i += 1                                               
    if res != 0:
        if res == 1:
            s_res = ""
        else:
            s_res = str(res)
        if deg > 1:
            return ("+" + s_res + variable + "^" + str(deg) if res > 0 else s_res + variable + "^" + str(deg))
        else:
            return ("+" + s_res + variable)
    else:
        return (None)

def ft_sum(members_list, variable, deg):
    if deg != 0:
        return (ft_sum_deg(members_list, variable, deg))
    elif deg == 0:                                                              #Sum-up digits
        return (ft_sum_deg_0(members_list, variable))
    
def ft_dispatch(members_list, variable):
    deg_0_list = []
    deg_1_list = []
    deg_2_list = []
    deg_3_list = []
    deg_4_list = []
    ordered_list = []
    for member in members_list:                                                 #Dispatch by degree
        if "^4" in member:
            deg_4_list.append(member)
        elif "^3" in member:
            deg_3_list.append(member)
        elif "^2" in member:
            deg_2_list.append(member)
        elif ("^1" in member or not ("^" in member)) and variable in member:
            deg_1_list.append(member)
        elif "^0" in member or (not ("^" in member) and not (variable in member)):
            deg_0_list.append(member)
        else:
            return ([])
    deg_4 = ft_sum(deg_4_list, variable, 4)
    deg_3 = ft_sum(deg_3_list, variable, 3)
    deg_2 = ft_sum(deg_2_list, variable, 2)                                     #Sum_up by degrees
    deg_1 = ft_sum(deg_1_list, variable, 1)
    deg_0 = ft_sum(deg_0_list, variable, 0)
    if deg_4:
        ordered_list.append(deg_4)
    if deg_3:
        ordered_list.append(deg_3)
    if deg_2:
        ordered_list.append(deg_2)
    if deg_1:
        ordered_list.append(deg_1)
    if deg_0:
        ordered_list.append(deg_0)
    if len(ordered_list) == 0:                                                  #If Null result
        ordered_list.append("0")
    return(ordered_list)

def ft_power(l_member, r_member, prefix):
    i = r_member
    res = l_member
    if r_member != 0:
        if r_member > 0:
            i = r_member - 1
        elif r_member < 0:
            i = r_member + 1
        while i:
            if r_member > 0:
                i -= 1
                res *= float(l_member)
            elif r_member < 0:
                i += 1
                res *= float(l_member)
        if r_member < 0:
            res = 1 / res
    else:
        res = 1
    return (prefix + str(res))

def ft_split_power(members_list):
    for idx, fact in enumerate(members_list):
        if "^" in fact and not (re.search("([a-zA-Z][\^])", fact)):
            i = 0
            j = 1
            for char in fact:
                if char == "^":
                    if char == "*" or char == "/":
                        j += 1
                    l_member = float(fact[j:i])
                    r_member = float(fact[i + 1:])
                    break
                i += 1
            members_list[idx] = ft_power(l_member, r_member, fact[:j])
    return(members_list)

def ft_prod_deg_0(members_list):
    res = 1
    for fact in members_list:
        if "^" in fact:
            splited = ft_split_power(members_list)                              #Power first
    for idx, fact in enumerate(members_list):
        if fact[0] == "*" or idx == 0:
            res *= float(fact[1 if idx != 0 else 0:])
        elif fact[0] == "/":
            res /= float(fact[1:])
    return(str(res))

def ft_split_prod_01_var(elem, variable, i):
    j = 0
    splited = []
    var = ""
    for char in elem:
        if char in "*/" or j == 0:
            k = j + 1
            var_start = -1
            var_end = 0
            while (k < len(elem) and not(elem[k] in "*/")):
                if i > 0 and elem[k] == variable:                               #Grab variable
                    var_start = k
                    var_end = k
                k += 1
                if i > 0 and var_start != -1:
                    var_end += 1
            splited.append(elem[j:k if var_start == -1 else var_start])
            if i > 0 and var_start != -1:                                       #Var to reintegrate
                var = elem[var_start]
        j += 1
    return (ft_prod_deg_0(splited) + var)
    
def ft_split_prod_more_vars(elem, variable, i):
    j = 0
    splited = []
    var = ""
    var_power = None
    for char in elem:
        if char in "*/" or j == 0:
            k = j + 1
            var_start = -1
            var_end = 0
            while (k < len(elem) and not(elem[k] in "*/")):
                if i > 0 and elem[k] == variable:                               #Grab variable
                    var_start = k
                    var_end = k
                k += 1
                if i > 0 and var_start != -1:
                    var_end += 1
            if var_power == None:
                if elem[var_end - 2] == "^":
                    var_power = int(elem[var_end - 1])
                else:
                    var_power = 1
            factor = elem[j:k if var_start == -1 else var_start]
            if not (variable in factor) and re.search("[0-9]", factor):
                splited.append(factor)
            if i > 0 and var_start != -1:                                       #Var to reintegrate
                var = elem[var_start]
                if elem[j] == "*":
                    if variable + "^" in var:
                        var_power += int(elem[var_end])
                    else:
                        var_power += 1
                elif elem[j] == "/":
                    if variable + "^" in var:
                        var_power -= int(elem[var_end])
                    else:
                        var_power -= 1
        j += 1
    if var_power != 0 and var_power != 1:
        var = var + "^" + str(var_power)
    elif var_power == 0:
        var = ""
    return (ft_prod_deg_0(splited) + var)

def ft_split_prod(members_list, variable):
    for idx, elem in enumerate(members_list):
        i = 0
        for char in elem:                                                       #Count vars
            if char == variable:
                i = i + 1
        if re.search("[*/]", elem):
            if i >= 2:                                                          #Prod degrees >= 2
                members_list[idx] = ft_split_prod_more_vars(elem, variable, i)
            else:                                                               #Prod degrees 0 and 1
                members_list[idx] = ft_split_prod_01_var(elem, variable, i)
    members_list = ft_split_power(members_list)                                 #Look for powers
    return(members_list)

def ft_split_sum(member, variable):
    splited = []
    i = 0
    while (i < len(member)):
        if member[i] in "+-" or i == 0:
            j = i + 1
            while (j < len(member) and (not(member[j] in "+-") \
                    or member[j - 1] in "/*^")):
                j += 1                                                          #Between each "+" or "-" (not preceded by "/" or "*"):
            signed = member[i:j]                                                #Slice a single member
            if not(member[i] in "+-") and i == 0:
                signed = "+" + signed                                           #Append "+" if needed
            splited.append(signed)
            i = j - 1
        i += 1
    i = 0
    for elem in splited:
        if elem == "-" and \
           i + 1 < len(splited) and \
           splited[i + 1][0] == "-":                                            #Turn "--" into "+" for next elem
            splited[i + 1] = splited[i + 1].replace("-", "+")
            splited.pop(i)
        i += 1
    splited = ft_split_prod(splited, variable)                                  #Make member product
    if splited:
        return (splited)
    else:
        return ([])

def ft_calculate(equation, variable):
    reduced = "None"
    equation = equation.replace(" ", "")
    reduced_list = equation.split("=")                                          #Split eq in 2
    if len(reduced_list) == 2:
        l_member = reduced_list[0]
        r_member = reduced_list[1]
        reduced_list = ft_split_sum(l_member, variable)                         #Split/Prod left members
        r_member = ft_split_sum(r_member, variable)                             #Split/Prod right members
        if reduced_list or r_member:
            if len(reduced_list) > 0:
                i = 0
                for elem in r_member:                                           #Rev r_member's sign
                    if elem[0] == "+":
                        r_member[i] = "-" + elem[1:]        
                    elif elem[0] == "-":
                        r_member[i] = "+" + elem[1:]
                    i += 1
            reduced_list += r_member                                            #Merge members
            reduced_list = ft_dispatch(reduced_list, variable)                  #Sum by degree
            if "=" in equation or [s for s in reduced_list if variable in s]:
                reduced = "".join(map(str, reduced_list)) + "=0"
            else:
                reduced = "".join(map(str, reduced_list))
        else:
            return("None", [])
    else:
        reduced_list = ft_split_sum(reduced_list[0], variable)
        reduced_list = ft_dispatch(reduced_list, variable)
        if "=" in equation or [s for s in reduced_list if variable in s]:
            reduced = "".join(map(str, reduced_list)) + "=0"
        else:
            reduced = "".join(map(str, reduced_list))
    if len(reduced) > 0 and reduced[0] == "+":                                  #remove first "+"
        reduced = reduced[1:]
    return(reduced, reduced_list)
    
