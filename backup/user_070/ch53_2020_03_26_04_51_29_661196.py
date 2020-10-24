def soma_impares(lista):
    soma = 0
    n = len(lista)
    i = 0
    while i < n:
        if lista[i]%2==1:
            soma += lista[i]
        i += 1
    return soma