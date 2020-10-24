def conta_bigramas(lista):
    dic = {}
    i=0
    bigrama = lista[i]+lista[i+1]
    for i in range(len(lista)-1):
        if bigrama not in dic:
            dic[bigrama]=1
        else:
            dic[bigrama]+=1
    return dic