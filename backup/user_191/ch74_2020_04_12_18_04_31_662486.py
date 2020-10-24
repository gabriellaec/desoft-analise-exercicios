def conta_bigramas(lista):
    dic = {}
    for i in range(len(lista)-1):
        bigrama = lista[i]+lista[i+1]
        if bigrama not in dic:
            dic[bigrama]=1
        else:
            dic[bigrama]+=1
    return dic