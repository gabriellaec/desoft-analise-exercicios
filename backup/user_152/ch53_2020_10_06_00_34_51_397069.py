def soma_impares(lista):
    soma = 0
    size = len(lista)
    if size>0:
        i = 0
        while i<size:
            if lista[i]%2 != 0:
                soma += lista[i]
            i += 1
    return soma