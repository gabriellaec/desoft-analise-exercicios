def soma_impares(lista):
    soma = 0
    for e in lista:
        if e%2 != 0:
            soma += e
    return soma
            