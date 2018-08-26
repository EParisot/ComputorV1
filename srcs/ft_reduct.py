# -*- coding: utf-8 -*-

import re

def ft_sum_deg_0(members_list):
    i = 0
    res = 0
    for elem in members_list:
        if re.match('^[+-]+$', elem):
            if elem[0] == "-" and \
               i + 1 < len(members_list) and \
               members_list[i + 1][0] == "-":                   #Turn "--" into "+" for next elem
                members_list[i + 1] = members_list[i + 1].replace("-", "+")
            res += 0
        elif re.match('^[0-9+-]+$', elem):
            res += int(elem)
        i = i + 1
    s_res = str(res)
    return ("+" + s_res if res > 0 else s_res)

def ft_sum_deg_1_2(members_list, variable, deg):
    res = 0
    for elem in members_list:
        i = 0
        for char in elem:
            if char == variable:                            #Sum-up factors
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

def ft_prod(member_list, variable):
    for elem in member_list:
        i = 0
        for char in elem:
            if char == variable:
                i = i + 1
        if "*" in elem or "/" in elem:
            if i > 0:
                #TODO make var product
                pass
            else:
                #TODO make simple product
                pass
    return(member_list)


def ft_split(member, variable):
    reduced_list = []
    i = 0
    while (i < len(member)):
        if member[i] in "+-" or i == 0:
            j = i + 1
            while (j < len(member) and not(member[j] in "+-")): #Between each "+" or "-":
                j = j + 1
            signed = member[i:j]                                #Slice a single member
            if not(member[i] in "+-") and i == 0:
                signed = "+" + signed                           #Append "+" if needed
            reduced_list.append(signed)
            i = j - 1
        i = i + 1
    reduced_list = ft_prod(reduced_list, variable)              #Make member product
    if reduced_list:
        return (reduced_list)
    else:
        return ([])

def ft_reduct(equation, variable):
    reduced = "None"
    equation = equation.replace(" ", "")
    reduced_list = equation.split("=")                          #Split eq in 2
    if len(reduced_list) == 2:
        l_member = reduced_list[0]
        r_member = reduced_list[1]
        reduced_list = ft_split(l_member, variable)             #Split/Prod left members
        r_member = ft_split(r_member, variable)                 #Split/Prod right members
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
        reduced_list = ft_split(reduced_list[0], variable)
        reduced_list = ft_dispatch(reduced_list, variable)
        if variable != "None":
            reduced = "".join(map(str, reduced_list)) + "=0"
        else:
            reduced = "".join(map(str, reduced_list))
    if len(reduced) > 0 and reduced[0] == "+":                  #remove first "+"
        reduced = reduced[1:]
    return(reduced, reduced_list)
    
