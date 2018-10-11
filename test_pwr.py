
def ft_exp(nb):
    res = 0
    #TODO
    return (res)

def ft_ln(nb):
    res = 0
    #TODO
    return (res)

def ft_power(l_member, r_member, prefix):
    res = ft_exp(r_member * ft_ln(l_member))
    return (prefix + str(res))

def ft_power_approx(l_member, r_member, prefix):
    i = r_member
    res = l_member
    if r_member != 0:
        if r_member > 0:
            i = r_member - 1
        elif r_member < 0:
            i = r_member + 1
        while i:
            if r_member > 0:
                if i - 1 < 0:

                    print(res, "+", round(i, 2), "*", float(ft_power_approx(l_member, round(r_member, 0) + 1, "")), "-", float(ft_power_approx(l_member, round(r_member, 0), "")), "=")

                    res += round(i, 2) * (float(ft_power_approx(l_member, round(r_member, 0) + 1, "")) - float(ft_power_approx(l_member, round(r_member, 0), "")))
                    i = 0
                else:
                    i -= 1
                    res *= float(l_member)
            elif r_member < 0:
                if i + 1 > 0:
                    res += i * (float(ft_power_approx(l_member, round(r_member, 0), "")) - float(ft_power_approx(l_member, round(r_member, 0) - 1, "")))
                    i = 0
                else:
                    i += 1
                    res *= float(l_member)
        if r_member < 0:
            res = 1 / res
    else:
        res = 1
    return (prefix + str(res))



print(ft_power_approx(2, 4.2, ""))
print(ft_power(2, 4.2, ""))
