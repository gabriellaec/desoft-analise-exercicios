def medias_por_inicial(l):
    medias = {}
    for k, v in l.items():
        if k[0] not in medias:
            medias[k[0]] = []
        medias[k[0]].append(v)
    
    for k in medias:
        medias[k] = sum(medias[k])/len(medias[k])
    
    return medias
