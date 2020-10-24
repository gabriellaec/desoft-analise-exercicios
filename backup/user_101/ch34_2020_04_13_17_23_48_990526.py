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
    r = n + 1
    l = range(r)
    ll = []
    for e in l:
        if avalia_primo(e) == True:
            ll.append(e)
    if len(ll) == 0:
        return -1
    else:
        m = max(ll)
        return m
