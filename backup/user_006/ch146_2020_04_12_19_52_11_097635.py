def conta_ocorrencias(lista):
    oco={}    
    i=0
    while i<len(lista):
        n=0
        for i in lista:
            if i==lista[i]:
            n=n+1
        oco[i]=n
    return oco    
        
    