def eh_primo(p):
    if p == 0:
        return False
    elif p == 1:
        return False
    if p == 2:
        return True
    elif p % 2 ==0:
        return False
    impares = 3
    while impares < p:
        if p % impares == 0:
            return False
        impares += 2
        return True

def lista_primos(n):
    lista = []
    i = 0
    while len(lista) < n :
        if eh_primo(i):
            primo_lista = lista.append(i)
        i += 1
    return primo_lista    