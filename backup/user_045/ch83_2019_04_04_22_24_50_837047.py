def medias_por_inicial(n):
    media={}
    for k in n:
        i=2
        if k[0] in media:
            media[k[0]]=(media[k[0]](i-1)+n[k])/i
            i+=1
        else:
            media[k[0]]=n[k]
    return media
            
       