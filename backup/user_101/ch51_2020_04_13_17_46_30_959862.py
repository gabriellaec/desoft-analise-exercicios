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
    c = b + 1
    todos_num = range(a, c)
    i = 0
    primos =[]
    while i < len(todos_num):
        if avalia_primo(todos_num[i]) == True:
            primos.append(todos_num[i])
        i += 1
    return primos
