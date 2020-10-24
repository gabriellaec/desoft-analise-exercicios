def conta_bigramas(lista):
    dicio = {}
    for ab in lista:
        if ab in dicio:
            dicio[ab] += 1
        else:
            dicio[ab]=1
    return dicio