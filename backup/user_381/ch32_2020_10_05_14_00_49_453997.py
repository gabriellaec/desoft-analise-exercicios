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

def lista_primos(n):
    lista_primo = []
    i = 1
    while len(lista_primo) < n:
        if eh_primo(i) == True:
            lista_primo.append(i)
        i += 1
    return lista_primo