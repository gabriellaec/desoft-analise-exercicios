def soma_impares(lista):
    soma = 0
    for e in lista:
        impar = e%2
        if impar != 0:
            soma += e
    return soma