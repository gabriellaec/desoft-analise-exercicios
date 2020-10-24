def inverte_lista(lista):
    inverte = []
    i = len(lista) - 1
    while i >= 0:
        inverte.append(lista[i])
        i -= 1
    return inverte