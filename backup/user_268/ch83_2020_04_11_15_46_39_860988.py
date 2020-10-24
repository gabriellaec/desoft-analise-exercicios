def medias_por_inicial(dic):
    new = {}
    chav = dic.keys()
    for i in chav:
        b = i[0]
        if not b in new:
            new[b] = dic[i]
        else:
            new[b] = (new[b] + dic[i])/2
    return new
        
    
    