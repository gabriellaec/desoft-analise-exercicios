def soma_impares(lista):
    s = 0
    for e in lista:
        if e%2 == 1:
            s += e
    return s