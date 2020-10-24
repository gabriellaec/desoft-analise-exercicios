def soma_impares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 != 0:
            soma += numero
    return soma