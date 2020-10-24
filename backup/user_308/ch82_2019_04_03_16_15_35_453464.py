def medias_por_inicial(medias):
    d={}
    for n in medias:
        if n[0] in d:
            d[n[0]]=(d[n[0]]+medias[n])/2
        else:
            d[n[0]]=medias[n]
    return d