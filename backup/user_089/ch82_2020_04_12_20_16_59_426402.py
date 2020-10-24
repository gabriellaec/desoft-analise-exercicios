def primeiras_ocorrencias(x):
    x = str(x)
    d = {}
    i = 0
    for e in x:
        if e not in d:
            d[e] = i 
              
        if e in d:
        i += 1
    return d