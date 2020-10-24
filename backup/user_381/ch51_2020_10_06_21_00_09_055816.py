def eh_primo(x):
    if x == 1:
        return False
    if x % 2 == 0 and x!=2:
        return False
    i=3
    while i<x:
        if x%i==0:
            return False
        i += 2
    return True

def primos_entre(a, b):
    lista_primos = []
    i = a
    while i >= a and i <= b:
        if eh_primo(i) == True:
            lista_primos.append(i)
        i += 1
    return lista_primos