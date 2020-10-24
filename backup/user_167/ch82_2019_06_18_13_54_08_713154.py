def primeiras_ocorrencias (string):
    d={}
    for e in string:
        if e not in d:
            d[e]=0
        d[e]+=1
    return d
            
    
            
        