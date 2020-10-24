def conta_ocorrencias(lista):
    oco={}    
    i=0
    for e in lista:
        n=0
        while i<len(lista):
            if e==lista[i]:
                n=n+1
        oco[e]=n
        i=i+1
    return oco    
        
    