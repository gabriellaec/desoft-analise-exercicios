def conta_bigramas(lista):
    dicio = {}
    for a in lista:
        if a in dicio:
            dicio[a] += 1
        else:
            dicio[a]=1
    return dicio