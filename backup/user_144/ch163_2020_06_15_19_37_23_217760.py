def calcula_media(dic):
    media = {}
    for i in dic:
        e = 2
        if dic[i] in media:
            media[i] = (media[i] + dic[i]) / e
            e += 1      
        else:
            media[i] = dic[i]        
    return media