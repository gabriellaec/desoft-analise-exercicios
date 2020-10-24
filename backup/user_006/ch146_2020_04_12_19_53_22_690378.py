def conta_ocorrencias(lista):
    oco={}    
    i=0
    while i<len(lista):
        n=0
        for e in lista:
            if e==lista[i]:
                n=n+1
        oco[e]=n
    return oco    
        
    