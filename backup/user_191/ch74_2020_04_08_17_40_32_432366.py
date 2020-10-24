def conta_bigramas(lista):
    for e in lista:
        if not e in dic:
            dic[e]=1
        else:
            dic[e]+=1
    return(dic)