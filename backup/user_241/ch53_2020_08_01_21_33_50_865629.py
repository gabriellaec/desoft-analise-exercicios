def soma_impares(lista):
    x = 0
    for i in lista:
        if i %2 == 1:
            x += i
    return x