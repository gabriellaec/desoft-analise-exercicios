def conta_ocorrencias(x):
    d = {}
    i = 0
    while i < len(x):
        
        d[x[i]] = i
        i = i + 1 
    return d