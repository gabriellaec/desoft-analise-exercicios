def conta_bigramas(palavra):
    d={}
    a=[]
    lista=list(palavra)
    i=0
    o=1
    while i<len(lista):
        a.append(lista[0]+lista[i])
        i+=1
        o+=1
        
    for e in a:
        if not in d:
            d[e]=1
        else:
            d[e]+=1
            
    return d
        