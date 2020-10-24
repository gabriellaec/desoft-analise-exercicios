def soma_impares(lista):
    impares = []
    size = len(lista)
    if size>0:
        i = 0
        while i<size:
            if lista[i]%2 != 0:
                impares.append(lista[i])
            i += 1
    return impares