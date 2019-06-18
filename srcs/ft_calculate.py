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
            #Sum-up factors
            if char == variable:
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
            return (sign + s_res + variable + "^" + \
                    str(deg) if res > 0 else s_res + variable + "^" + str(deg))
        else:
            return (sign + s_res + variable)
    else:
        return (None)

def ft_sum(members_list, variable, deg):
    if deg != 0:
        return (ft_sum_deg(members_list, variable, deg))
    #Sum-up digits
    elif deg == 0:
        return (ft_sum_deg_0(members_list, variable))
    
def ft_dispatch(members_list, variable):
    deg_dict = {}
    for member in members_list:
        if "^" in member:
            power, start = ft_get_power(member, variable)
            if str(power) not in deg_dict:
                deg_dict[str(power)] = []
            deg_dict[str(power)].append(member)
        elif variable in member:
            if "1.0" not in deg_dict:
                deg_dict["1.0"] = []
            deg_dict["1.0"].append(member)
        elif variable not in member:
            if "0.0" not in deg_dict:
                deg_dict["0.0"] = []
            deg_dict["0.0"].append(member)
    key_list = []
    deg_lists = []
    for key in sorted(deg_dict.keys()):
        key_list.append(key)
        deg_lists.append(deg_dict[key])
    
    #Sum_up by degrees
    sums_list = [None for _ in range(len(deg_lists))]
    ordered_list = []
    for deg in range(len(deg_lists)-1, -1, -1):
        sums_list[deg] = ft_sum(deg_lists[deg], variable,\
                                int(key_list[deg].split(".")[0]))
        if sums_list[deg]:
            ordered_list.append(sums_list[deg])
    #If Null result
    if len(ordered_list) == 0:
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
                if ft_abs(i * i - number) < 0.01:
                    return(i)
                i += prec
            i = 0
            prec /= 10
        return (0)

def ft_power(l_member, r_member, prefix):
    i = r_member
    res = l_member
    if r_member != 0:
        if r_member % 1 != 0:
            res = l_member ** r_member
        elif r_member > 0:
            i = r_member - 1
        elif r_member < 0:
            i = r_member + 1
        while i and i % 1 == 0:
            if r_member > 0:
                i -= 1
                res *= float(l_member)
            elif r_member < 0:
                i += 1
                res *= float(l_member)
        if r_member < 0 and i % 1 == 0:
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
        #Power first
        if "^" in fact:
            ft_split_power(members_list)
    for idx, fact in enumerate(members_list):
        if fact[0] == "*":# or idx == 0:
            if len(fact) > 1:
                res *= float(fact[1 if idx != 0 else 0:])
        elif fact[0] == "/":
            if len(fact) > 1:
                res /= float(fact[1:])
            else:
                res = str(res) + "/"
        elif idx == 0:
            if len(fact) > 1:
                res *= float(fact[1 if idx != 0 else 0:])
    return(str(res))

def ft_split_prod_01_var(elem, variable, i):
    splited = []
    var = ""
    for j, char in enumerate(elem):
        if char in "*/" or j == 0:
            k = j + 1
            var_start = -1
            var_end = 0
            #Grab variable
            while (k < len(elem) and not(elem[k] in "*/")):
                if i > 0 and elem[k] == variable:
                    var_start = k
                    var_end = k
                k += 1
                if i > 0 and var_start != -1:
                    var_end += 1
            splited.append(elem[j:k if var_start == -1 else var_start])
            #Var to reintegrate
            if i > 0 and var_start != -1:
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
                #Grab variable
                if i > 0 and elem[k] == variable:
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
            #Var to reintegrate
            if i > 0 and var_start != -1:
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
        for char in elem:
            #Count vars
            if char == variable:
                i = i + 1
        if re.search("[*/]", elem):
            if i >= 2:
                #Prod degrees >= 2
                members_list[idx] = ft_split_prod_more_vars(elem, variable, i)
            else:
                #Prod degrees 0 and 1
                members_list[idx] = ft_split_prod_01_var(elem, variable, i)
    #Look for powers
    members_list = ft_split_power(members_list)
    return(members_list)

def ft_split_sum(member, variable):
    splited = []
    i = 0
    while (i < len(member)):
        if member[i] in "+-" or i == 0:
            j = i + 1
            #Between each "+" or "-" (not preceded by "/" or "*")
            while (j < len(member) and (not(member[j] in "+-") \
                    or member[j - 1] in "/*^")):
                j += 1
            if member[i:j] != "0":
                #Slice a single member
                signed = member[i:j]
                #Append "+" if needed
                if not(member[i] in "+-") and i == 0:
                    signed = "+" + signed                                       
                splited.append(signed)
                i = j - 1
        i += 1
    i = 0
    #Turn "--" into "+" for next elem
    for elem in splited:
        if elem == "-" and i + 1 < len(splited) and splited[i + 1][0] == "-":
            splited[i + 1] = splited[i + 1].replace("-", "+")
            splited.pop(i)
        i += 1
    #Make member product
    splited = ft_split_prod(splited, variable)
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

def clean_zeros(member_list, variable):
    for i, elem in enumerate(member_list):
        if variable + "^0.0" in elem:
            var_pow, start = ft_get_power(elem, variable)
            member_list[i] = elem[:start-2]
    return member_list

def clean_powers(member_list, variable):
    #Make "/x" or "x^-1" dissapear
    idx = -1
    power = 0
    for i, elem in enumerate(member_list):
        if "/" + variable in elem:
            new_pow = 1
            if variable + "^" in elem:
                new_pow, start = ft_get_power(elem, variable)
                new_pow -= 1
                member_list[i] = elem[:start - 1]
                member_list[i] = member_list[i].replace("/" + variable, variable + "^" + str(new_pow))
            else:
                member_list[i] = member_list[i].replace("/" + variable, "")
                power = new_pow
            idx = i
        elif variable + "^-" in elem:
            idx = i
        i = 0
    return (member_list, idx, power)

def ft_distrib_div(l_member_list, r_member_list, variable):
    clean_zeros(l_member_list, variable)
    clean_zeros(r_member_list, variable)
    l_member_list, idx, power = clean_powers(l_member_list, variable)
    i = 0
    #Calc new powers by distribution
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
                            l_member_list[i] = l_member_list[i][:j-1] + \
                                    variable + "^" + str(other_power)
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
        #Apply new powers
        for k, elem in enumerate(r_member_list):
            if not (variable in elem):
                r_member_list[k] += variable + \
                        ("^" + str(power) if power != 0 and power != 1 else "")
            else:
                if not ("^" in elem):
                    r_member_list[k] += "^" + str(1 + power)
                else:
                    var_pow, start = ft_get_power(elem, variable)
                    r_member_list[k] = \
                        r_member_list[k][:start] + str(var_pow + power)
    return clean_zeros(l_member_list, variable), clean_zeros(r_member_list, variable)

def ft_reduce_members(equation, members_list, variable):
    l_member = members_list[0]
    r_member = members_list[1]
    #Split/Prod left members
    l_member_list = ft_split_sum(l_member, variable)
    #Split/Prod right members
    r_member_list = ft_split_sum(r_member, variable)
    run = True
    while run:
        #Dispatch divisions
        run = False
        l_member_list, r_member_list = \
                       ft_distrib_div(l_member_list, r_member_list, variable)
        r_member_list, l_member_list = \
                       ft_distrib_div(r_member_list, l_member_list, variable)
        #While there is negative division
        for elem in l_member_list + r_member_list:
            if variable + "^-" in elem:
                run = True
    if l_member_list or r_member_list:
        if len(l_member_list) > 0:
            i = 0
            for elem in r_member_list:
                #Rev r_member's sign
                if elem[0] == "+":
                    r_member_list[i] = "-" + elem[1:]     
                elif elem[0] == "-":
                    r_member_list[i] = "+" + elem[1:]
                elif elem[0] != "+" and elem[0] != "-":
                    r_member_list[i] = "-" + elem
                i += 1
        #Merge members
        l_member_list += r_member_list
        #Sum by degree
        l_member_list = ft_dispatch(l_member_list, variable)
        if "=" in equation or [s for s in l_member_list if variable in s]:
            reduced = "".join(map(str, l_member_list)) + "=0"
        else:
            reduced = "".join(map(str, l_member_list))
    else:
        return("None", [])
    return(reduced, l_member_list)

def ft_calculate(equation, variable, is_par):
    reduced = "None"
    equation = equation.replace(" ", "")
    #Split eq in 2
    members_list = equation.split("=")
    #Reduce to one member
    if len(members_list) == 2:
        reduced, l_member_list = \
                 ft_reduce_members(equation, members_list, variable)
    else:
        l_member_list = ft_split_sum(members_list[0], variable)
        l_member_list = ft_dispatch(l_member_list, variable)
        if "=" in equation or [s for s in l_member_list if variable in s]\
           and is_par == False:
            reduced = "".join(map(str, l_member_list)) + "=0"
        else:
            reduced = "".join(map(str, l_member_list))
    #remove first "+"
    if len(reduced) > 0 and reduced[0] == "+":
        reduced = reduced[1:]
    if reduced == "0=0" and variable != "None":
        reduced = variable + " = " + variable
    return(reduced, l_member_list)
