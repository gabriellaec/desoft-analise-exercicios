def soma_impares(lista):
    s = 0
    for i in range(lista):
        if lista[i] % 2 != 0:
            s+=lista[i]
    return s
            