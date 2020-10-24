def conta_ocorrencias(lista):
    oco={}    
    i=0
    for e in lista:
        n=0
        for i in lista:
            if e==i:
                n=n+1
        oco[e]=n
    return oco    
        
    