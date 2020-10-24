def medias_por_inicial(dic):
    med={}
    for k, v in dic.items():
        if k[0] not in med:
            med[k[0]]=v
        elif k[0] in med:
            med[k[0]]+=v
            
    return med