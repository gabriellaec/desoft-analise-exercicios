def medias_por_inicial(dic):
    new = {}
    chav = dic.keys()
    for i in range(len(chav)):
        a = chav[i]
        b = a[0]
        if not b in new:
            new[b] = dic[i]
        else:
            new[b] = (new[b] + dic[i])/2
    return new
        
    
    