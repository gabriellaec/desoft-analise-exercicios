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
    contador = 1
    while len(lista_primo) < n:
        if eh_primo(contador) == True:
            lista_primo.append(contador)
        contador += 1
    return lista_primo