def soma_impares(lista):
    i = 0
    s = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            s += lista[i]
    return s
            