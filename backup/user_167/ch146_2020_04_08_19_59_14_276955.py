def conta_ocorrencias (lista):
    d={}

    for e in lista:
        if e not in d:
            d[e]=1
        else:
            d[e]+=1
        
    