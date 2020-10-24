def soma_impares(lista):
    X = len(lista)
    soma = 0
    for n in range (X):
        if lista[n] % 2 != 0:
            soma += lista[n]
    return soma