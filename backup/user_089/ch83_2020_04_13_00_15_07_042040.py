def medias_por_inicial(dic):
    novo = {}
    n = []
    for k,v in dic.items():
        if k[0] in novo:
            float(novo[k[0]]) += v 
            float(novo[k[0]]) = float(novo[k[0]])/len(n)
         
        if k[0] not in novo:
            float(novo[k[0]]) = v
            n.append(1)
    return novo 
        
        
       
    
                     