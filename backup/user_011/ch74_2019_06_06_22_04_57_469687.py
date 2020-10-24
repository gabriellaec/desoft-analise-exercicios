def conta_bigramas(lista):
    dici = {}
    i = 1
    while i < len(lista):
        a = str(lista[i-1]) + str(lista[i])
        if a not in dici:
            dici[a] = 0
        if a in dici:
            dici[a] += 1
        i += 1
    return dici