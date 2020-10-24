def medias_por_inicial(dic):
    novo = {}
    n = []
    for k in dic:
        if k[0] in novo:
            novo[k[0]] += dic[k]
            n.append
        
        if k[0] not in novo:
            novo[k[0]] = dic[k]
            n.append(1)
    for k,v in novo.items():
        novo[k] = novo[k]/len(n)
        
    return novo 
        
        
       
    
                     