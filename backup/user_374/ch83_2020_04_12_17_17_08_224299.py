def medias_por_inicial(l1):
    dicionario = {}
    dic2 = {}
    for k, v in l1.items():
       
        a = k
        b = v
        if a[0] not in dicionario:
            dicionario[a[0]] = b
            dic2[a[0]] = 1
            
            
        else: 
            dicionario[a[0]] = (dicionario[a[0]]+b)
            dic2[a[0]] += 1
    
    for k in dicionario:
        dicionario[k]= dicionario[k]/dic2[k]
    
    return dicionario
        