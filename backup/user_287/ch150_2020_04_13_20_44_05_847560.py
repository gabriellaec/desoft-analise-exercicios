import math
def calcula_pi(n):
    if n == 1:
        p = (6**(1/2))
    return p
    p = 0
    ran = list(range(n))
    ran.remove(0)
    for a in (ran):
        p += (6/(a**2))
        p = (p**(1/2))
        return p