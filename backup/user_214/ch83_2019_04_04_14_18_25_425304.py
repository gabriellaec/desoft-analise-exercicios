def medias_por_inicial(dic):
    media={}
    for a in dic:
        i=2
        if a[0] in media:
            media[a[0]]=(media[a[0]]+dic[a])/i
            i+1
        else:
            media[a[0]]=dic[a]
    return media