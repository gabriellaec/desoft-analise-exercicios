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
                           

def primos_entre(a, b):
    l_primos = []
    c = b + 1
    nums = range(a, c)
    for e in nums:
        n = avalia_primo(e)
        if n == True:
            l_primos.append(n)
    quant = len(l_primos)
    return quant
