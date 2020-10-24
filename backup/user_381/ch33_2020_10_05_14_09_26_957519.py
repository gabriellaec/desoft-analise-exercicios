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
    i = 0
    while i <= a and i >= b:
        if eh_primo = True:
            lista_primos.append(i)
        i += 1
    return len(lista_primos)