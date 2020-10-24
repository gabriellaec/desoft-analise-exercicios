def soma_impares(lista):
    x= len(lista)
    i = 0
    soma = 0
    while i != x:
        if lista[i] %2 != 0:
            soma += lista[i]
            i += 1
        else:
            i += 1
    return soma 