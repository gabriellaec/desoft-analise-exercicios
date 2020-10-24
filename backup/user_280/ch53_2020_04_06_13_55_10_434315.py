def soma_impares(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i]%2 == 0:
            soma += 0
        else:
            soma += lista[i]
    return soma
            