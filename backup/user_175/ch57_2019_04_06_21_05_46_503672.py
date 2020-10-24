def soma_impares(lista):
    lista_impares = []
    i = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            lista_impares.append(lista[i])
        i += 1 
    soma = 0
    n = 0
    while n < len(lista_impares):
        soma += lista_impares[n]
        n += 1
    return soma