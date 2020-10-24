def medias_por_inicial(dicio):
    d = {}
    for k,v in dicio.items():
        d[k[0]] = v
    return d