def medias_por_inicial(dic):
    media = {}
    for i in dic:
        e = 2
        if i[0] in media:
            media[i[0]] = (media[i[0]] + dic[i]) / e
            e += 1      
        else:
            media[i[0]] = dic[i]        
    return media