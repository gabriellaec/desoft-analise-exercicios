def soma_impares(lista):
    saida = 0
    for e in lista:
        if e%2!=0:
            saida += e
    return saida
