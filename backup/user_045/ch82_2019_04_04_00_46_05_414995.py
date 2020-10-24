def primeiras_ocorrencias(n):
    d={}
    i=0
    for e in n:
        if e not in d:
            d[e]=i
        i+=1
    return d