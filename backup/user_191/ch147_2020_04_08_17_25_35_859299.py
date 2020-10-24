def mais_frequente(lista):
    dic={}
    for e in lista:
        if not e in dic:
            dic[e]=1
        else:
            dic[e]+=1
        v=list(dic.values())
        k=list(dic.keys())
        return k[v.index(max(v))]