def conta_bigramas(string):
    dic={}
    bigrama=[]
    lista=list(string)
    i=1
    u=0
    while i<len(lista):
        bigrama.append(lista[u]+lista[i])
        i+=1
        u+=1
    for e in bigrama:
        if e not in dic:
            dic[e]=1
        else:
            dic[e]+=1
    return dic
    