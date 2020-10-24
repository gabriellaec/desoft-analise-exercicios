def medias_por_inicial(dicio):
    media={}
    for k in dicio:
        i=1
        if k[0] in media:
            media[k[0]]=(media[k[0]]*(i-1)+dicio[k])/i
            i+=1
        else:
            media[k[0]]=dicio[k]
    return media