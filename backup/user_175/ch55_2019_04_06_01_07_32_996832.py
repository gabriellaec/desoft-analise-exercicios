from math import sqrt 

def eh_primo(x):
    x = int(x)
    if x == 2:
        return True
    elif x < 2:
        return False
    t = 2
    while t < x:
        if x % t == 0:
            return False
        elif x % t != 0:
            t += 1
    return True
    
def primos_entre(a, b):
    lista = []
    x = int(a)
    y = int(b)    
    while x <= y:
        if eh_primo(x) == True:
            lista.append(x)
        x += 1
    return lista