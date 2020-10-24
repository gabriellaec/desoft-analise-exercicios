def soma_impares(lista):
    soma = 0
    for i in lista:
        if not i % 2 == 0:
            soma += i
    return soma