def conta_bigramas(lista):
    dici = {}
    i = 1
    j = 0
    while i <= len(lista) and j<len(lista):
        a = str(lista[i]) + str(lista[i-1])
        if a not in dici:
            dici[j] = 0
        if a in dici:
            dici[j] += 1
        i += 1
        j += 1
        