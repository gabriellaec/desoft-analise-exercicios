def medias_por_inicial(medias):
    d={}
    for n,m in medias.terms():
        d[n[0]]=m
    return d