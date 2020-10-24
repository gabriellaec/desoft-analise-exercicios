def medias_por_inicial(dici):
    novo = dict()
    i = 0
    for k, v in dici.items():
        if k[i] in novo:
            novo[k[i]] += (k[i] +v)/2
        else:
            novo[k[i]] = v/i
    	i += 1
    return novo