def conta_bigramas(palavra):
    d={}
    a=[]
    i=1
    o=0
    while i<len(paalavra):
        a.append(lista[o]+lista[i])
        i+=1
        o+=1
        
    for e in a:
        if e not in d:
            d[e]=1
        else:
            d[e]+=1
    return d
        