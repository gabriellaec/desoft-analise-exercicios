def soma_impares(lista):
    s = 0
    for i in lista:
        if lista[i] % 2 != 0:
            s+=lista[i]
    return s
            