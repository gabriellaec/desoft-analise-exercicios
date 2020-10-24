def soma_impares(lista):
    liss = []
    i = 0
    while i<len(lista):
        if lista[i]%2 == 0:
            i = i + 1
        else liss.append(lista[i])
        i = i + 1
    return liss