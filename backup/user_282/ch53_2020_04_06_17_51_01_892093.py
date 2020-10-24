def soma_impares(lista):
    impar = []
    for e in lista:
        if e % 2 != 0:
            impar.append(e)
    return impar