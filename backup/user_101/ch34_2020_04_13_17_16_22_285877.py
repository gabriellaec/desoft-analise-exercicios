from math import *

def avalia_primo(z):
    x = fabs(z)
    if x == 2:
        return True
    elif x < 2:
        return False
    elif x % 2 == 0:
        return False
    else:
        l = range(2, z)
        aval = []
        for e in l:
            if z % e == 0:
                aval.append(False)
        if False in aval:
            return False
        else:
            return True
                           

def maior_primo_menor_que(n):
    l = range(n + 1)
    for e in l:
        if avalia_primo(e) == False:
            del e
    if len(l) == 0:
        return -1
    else:
        m = max(l)
        return m
