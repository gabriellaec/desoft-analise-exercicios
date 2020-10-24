def primeiras_ocorrencias(x):
    
    z = dict()
    
    
    for i in range(len(x)):
        if x[i] not in z:
           z[x[i]] = i
            
    return z
    