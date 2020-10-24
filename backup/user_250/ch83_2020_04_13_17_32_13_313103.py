def medias_por_inicial(lista):
    dicA = {}
    dicB = {}
    dicionario = {}
    for k, v in lista.items():
        x = k
        y = v
        i = 0
        if x[i] not in dicA:
            dicA[x[i]] = y
            dicB[x[i]] = 1
        else:
            dicA[x[i]] = dicA[x[0]]+y
            dicB[x[i]] += 1
        i += 1
    for k in dicA:
        dicionario[k] = dicA[k]/dicB[k]
    return dicionario