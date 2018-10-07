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
        if res < 0:
            sign = ""
        else:
            sign = "+"
        return (sign + s_res if res > 0 else s_res)
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
        if res < 0:
            sign = ""
        else:
            sign = "+"
        if deg > 1:
            return (sign + s_res + variable + "^" + str(deg) if res > 0 else s_res + variable + "^" + str(deg))
        else:
            return (sign + s_res + variable)
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

def ft_get_power(elem, variable):
    for n, char in enumerate(elem):
        if char == "^" and elem[n-1] == variable:
            power = float(elem[n+1:])
            start = n + 1
    return (power, start)

def ft_abs(number):
    if number > 0:
        return(number)
    else:
        return(-number)

def ft_sqrt(number):
    if number > 0:
        prec = 1
        i = 0
        while (prec >= 0.0001):
            while i * i <= number:
                if ft_abs(i * i - number) < 0.001:
                    return(i)
                i += prec
            i = 0
            prec /= 10
        return (0)

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
            j = 0
            for char in fact:
                if char == "*" or char == "/":
                    j += 1
                if char == "^":
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
            if len(fact) > 1:
                res *= float(fact[1 if idx != 0 else 0:])
            else:
                res = str(res)
        elif fact[0] == "/":
            if len(fact) > 1:
                res /= float(fact[1:])
            else:
                res = str(res) + "/"
    return(str(res))

def ft_split_prod_01_var(elem, variable, i):
    splited = []
    var = ""
    for j, char in enumerate(elem):
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
                if "^1" in var:
                    var = elem[var_start]                   
                else:
                    var = elem[var_start:var_end]
    return (ft_prod_deg_0(splited) + var)
    
def ft_split_prod_more_vars(elem, variable, i):
    splited = []
    var = ""
    var_power = None
    for j, char in enumerate(elem):
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
                if variable + "^" in elem[var_start:var_end]:
                    var_power = int(elem[var_end - 1])
                else:
                    var_power = 1
            factor = elem[j:k if var_start == -1 else var_start]
            if not (variable in factor) and re.search("[0-9]", factor):
                splited.append(factor)
            if i > 0 and var_start != -1:                                       #Var to reintegrate
                var = elem[var_start]
                if elem[j] == "*":
                    if variable + "^" in elem[var_start:var_end]:
                        var_power += int(elem[var_end - 1])
                    else:
                        var_power += 1
                elif elem[j] == "/":
                    if variable + "^" in elem[var_start:var_end]:
                        var_power -= int(elem[var_end - 1])
                    else:
                        var_power -= 1
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
            if member[i:j] != "0":
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

def ft_iseven_par(member):
    count = 0
    for char in member:
        if char in "()":
            count += 1
    return(True if count % 2 == 0 else False)

def deal_with_par(members_list, variable):
    for n, member in enumerate(members_list):
        while "(" in member and ")" in member:
            for idx, char in enumerate(member):
                if char == "(":
                    i = 0
                    start = idx + 1
                    for idx, char in enumerate(member[start:]):
                        if char == "(":
                            i += 1
                        elif char == ")" and i > 0:
                            i -= 1
                        elif char == ")" and i == 0:
                            end = start + idx
                            break
            if not ("(" in member[1:-1] or ")" in member[1:-1]):
                members_list[n] = member[1:-1]
                break
            reduced_par, reduced_list = ft_calculate(member[start:end], variable, True)
            if len(ft_split_sum(reduced_par, variable)) > 1:
                others = members_list[n].replace(member[start - 1:end + 1], "__").split("_")
                k = 0
                for item, element in enumerate(others):
                    if len(element) == 0:
                        if k != 0:
                            others.pop(item)
                        k += 1
                i = 0
                for idx, other in enumerate(others):
                    if len(other) == 0:
                        i = idx
                        break
                j = 0
                idx = 0
                for other in others:
                    if len(other) > 0:
                        new_reduced_par = ft_split_sum(reduced_par, variable)
                        if idx == i - 1:
                            if not (other[-1] in "+-"):
                                if other[0] == "(" and ft_iseven_par(other) == False:
                                    other = other[1:]
                                    others[idx] = "("
                                if len(other) > 0 and other[0] != "-":
                                    other = "+" + other
                                if len(other) > 0:
                                    for idx2, elem in enumerate(new_reduced_par):
                                        if len(other) > 0 and not (other[-1] in "*/^"):
                                            other = other + "*"
                                        new_reduced_par[idx2] = other + elem
                                    others[i] = "".join(map(str, new_reduced_par))
                                    if others[i - 1 if i - 1 >= 0 else 0] != "(":
                                        others.pop(i - 1)
                                    j += 1
                            else:
                                others[i] = reduced_par
                                member = members_list[n] = "".join(map(str, others))
                        elif idx == i + 1:
                            if not (other[0] in "+-)"):
                                if other[-1] == ")" and ft_iseven_par(other) == False:
                                    other = other[:-1]
                                    others[idx] = ")"
                                if len(other) > 0:
                                    for idx2, elem in enumerate(new_reduced_par):
                                        new_reduced_par[idx2] = elem + other
                                    others[i] = "".join(map(str, new_reduced_par))
                                    others.pop(i + 1)
                                    j += 1
                            elif other[0] in "+-":
                                others[i] = reduced_par
                                member = members_list[n] = "".join(map(str, others))
                            break
                    idx += 1
                if j == 0:
                    others[i] = member[start - 1:end + 1]
                members_list[n] = "".join(map(str, others))
            else:
                members_list[n] = members_list[n].replace(member[start - 1:end + 1], reduced_par)
            member = members_list[n]
    return(members_list)

def ft_distrib_div(l_member_list, r_member_list, variable):
    idx = -1
    power = 0
    for i, elem in enumerate(l_member_list):
        if "^0.0" in l_member_list[i]:
            var_pow, start = ft_get_power(elem, variable)
            l_member_list[i] = l_member_list[i][:start-2]
        if "/" + variable in elem:
            new_pow = 1
            if variable + "^" in elem:
                new_pow, start = ft_get_power(elem, variable)
                new_pow -= 1
                l_member_list[i] = elem[:start - 1]
                l_member_list[i] = l_member_list[i].replace("/" + variable, variable + "^" + str(new_pow))
            else:
                l_member_list[i] = l_member_list[i].replace("/" + variable, "")
                power = new_pow
            idx = i
        elif variable + "^-" in elem:
            idx = i
        i = 0
    if idx != -1:
        while i < len(l_member_list):
            if i == idx or "^-" in l_member_list[i]:
                for j, char in enumerate(l_member_list[i]):
                    if char == "^" and l_member_list[i][j - 1] == variable:
                        if i == idx:
                            power = float(l_member_list[i][j + 1:])
                            if power == -1.0:
                                power = 1.0
                            else:
                                power += 1
                            l_member_list[i] = l_member_list[i][:j-1]
                        else:
                            other_power = float(l_member_list[i][j + 1:]) - power
                            if other_power == -1.0:
                                other_power = 1.0
                            else:
                                other_power += 1
                            l_member_list[i] = l_member_list[i][:j-1] + variable + "^" + str(other_power)
            else:
                if l_member_list[i][0] == "-":
                    r_member_list.append("+" + l_member_list[i][1:])
                elif l_member_list[i][0] == "+":
                    r_member_list.append("-" + l_member_list[i][1:])
                elif l_member_list[i][0] != "+" and l_member_list[i][0] != "-":
                    r_member_list.append("-" + l_member_list[i])
                l_member_list.pop(i)
                if idx > i:
                    idx -= 1
                i -= 1
            i += 1
        for k, elem in enumerate(r_member_list):
            if not (variable in elem):
                r_member_list[k] += variable + ("^" + str(power) if power != 0 and power != 1 else "")
            else:
                if not ("^" in elem):
                    r_member_list[k] += "^" + str(1 + power)
                else:
                    var_pow, start = ft_get_power(elem, variable)
                    r_member_list[k] = r_member_list[k][:start] + str(var_pow + power)
    #print(l_member_list, r_member_list)
    return l_member_list, r_member_list

def ft_calculate(equation, variable, is_par):
    reduced = "None"
    equation = equation.replace(" ", "")
    members_list = equation.split("=")                                          #Split eq in 2
    members_list = deal_with_par(members_list, variable)                        #Deal with '()'
    if len(members_list) == 2:
        l_member = members_list[0]
        r_member = members_list[1]
        l_member_list = ft_split_sum(l_member, variable)                        #Split/Prod left members
        r_member_list = ft_split_sum(r_member, variable)                        #Split/Prod right members
        l_member_list, r_member_list = ft_distrib_div(l_member_list, r_member_list, variable)
        r_member_list, l_member_list = ft_distrib_div(r_member_list, l_member_list, variable)
        if l_member_list or r_member_list:
            if len(l_member_list) > 0:
                i = 0
                for elem in r_member_list:                                      #Rev r_member's sign
                    if elem[0] == "+":
                        r_member_list[i] = "-" + elem[1:]     
                    elif elem[0] == "-":
                        r_member_list[i] = "+" + elem[1:]
                    elif elem[0] != "+" and elem[0] != "-":
                        r_member_list[i] = "-" + elem
                    i += 1
            l_member_list += r_member_list                                      #Merge members
            l_member_list = ft_dispatch(l_member_list, variable)                #Sum by degree
            if "=" in equation or [s for s in l_member_list if variable in s] and is_par == False:
                reduced = "".join(map(str, l_member_list)) + "=0"
            else:
                reduced = "".join(map(str, l_member_list))
        else:
            return("None", [])
    else:
        l_member_list = ft_split_sum(members_list[0], variable)
        l_member_list = ft_dispatch(l_member_list, variable)
        if "=" in equation or [s for s in l_member_list if variable in s] and is_par == False:
            reduced = "".join(map(str, l_member_list)) + "=0"
        else:
            reduced = "".join(map(str, l_member_list))
    if len(reduced) > 0 and reduced[0] == "+":                                  #remove first "+"
        reduced = reduced[1:]
    return(reduced, l_member_list)
