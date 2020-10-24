def medias_por_inicial(dic):
    novo = {}
    n = []
    for k,v in dic.items():
        if k[0] in novo:
            novo[k[0]] += v 
            novo[k[0]] = (novo[k[0]])/len(n)
         
        if k[0] not in novo:
            novo[k[0]] = v
            n.append(1)
    return novo 
        
        
       
    
                     