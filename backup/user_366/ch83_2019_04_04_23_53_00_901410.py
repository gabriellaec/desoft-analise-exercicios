def medias_por_inicial(dici):
    novo = dict()
    for k, v in dici.items():
        if k[0] not in novo:
            novo[k[0]] = v 
        else:
            novo[k[0]] = (novo[k[0]]+v)/2
    return novo