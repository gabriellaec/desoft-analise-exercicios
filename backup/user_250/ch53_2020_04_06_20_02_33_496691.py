soma = 0
def soma_impares(lista):
    for e in lista:
        if e%2 != 0:
            soma += e
            return soma
            