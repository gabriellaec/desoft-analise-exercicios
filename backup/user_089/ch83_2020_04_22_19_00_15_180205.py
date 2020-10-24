def medias_por_inicial(dic):
    novo = {}
    n = []
    for k in dic:
        if k[0] in novo:
            novo[k[0]] += dic[k]
            n.append(1)
        
        if k[0] not in novo:
            novo[k[0]] = dic[k]
            n.append(1)
    for e in novo:
        e = e/len(n)
        
    return novo 
        
        
       
    
                     