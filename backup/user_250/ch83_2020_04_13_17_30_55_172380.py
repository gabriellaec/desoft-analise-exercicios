def medias_por_inicial(lista):
    dicA = {}
    dicB = {}
    dicionario = {}
    for k, v in lista.items():
        x = k
        y = v
        if x[0] not in dicA:
            dicA[x[0]] = b
            dicB[x[0]] = 1
        else:
            dicA[x[0]] = dicA[x[0]]+b
            dicB[x[0]] += 1
    for k in dictA:
        dicionario[k] = dictA[k]/dictB[k]
    return dicionario