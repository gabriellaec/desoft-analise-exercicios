import numpy as np
def lista_primos(n):
    primos = []
    t = 0
    while n < len(primos):
        if t == 0 or t == 1:
            return False
        elif t%2==0 and t!=2:
            return False
        else:
            i = 3
            while i < t:
                if t%i==0:
                    return False
                i += 2
            return True
            primos.append(t)
    t += 1
    return lista_primos
print(lista_primos(10))