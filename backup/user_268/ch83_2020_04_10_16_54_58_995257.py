def medias_por_inicial(dic):
    new = {}
    chav = keys(dic)
    vlr = values(dic)
    for i in range(len(chav)):
        a = chav[i][0]
        if not a in new:
            new[a] = dic[i]
        else:
            new[a] = (new[a] + dic[i])/2
    return new
        
    
    