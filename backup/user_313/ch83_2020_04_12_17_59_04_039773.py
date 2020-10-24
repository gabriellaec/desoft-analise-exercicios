def medias_por_inicial(l1):
    
    dicionario = {}
    novodicionario = {}
    novodicionario['conta'] = 1

    for k, v in l1.items():
        
        a = k
        b = v
        
        if a[0] not in dicionario:
            dicionario[a[0]] = b
            

        else:
            
            novodicionario['conta'] += 1
            dicionario[a[0]] = (dicionario[a[0]]+b)
            
            
    for i in dicionario.keys():
        if dicionario[i] > 10:
            dicionario[i] = dicionario[i]/novodicionario['conta']
                    
            
    
    return dicionario
