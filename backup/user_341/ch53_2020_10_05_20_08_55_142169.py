def soma_impares(lista):
    k = 0
    liss = []
    i = 0
    while i<len(lista):
        if lista[i]%2 == 0:
            i = i + 1
        else:
            liss.append(lista[i])
            i = i + 1
    for j in liss:
        k += j
    return k