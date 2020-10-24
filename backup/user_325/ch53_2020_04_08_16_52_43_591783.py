def soma_impares(lista):
    s = 0
    for i in lista:
        if i % 2 != 0:
            s+=i
    return s
            