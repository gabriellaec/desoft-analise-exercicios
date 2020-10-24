def mais_frequente(lista):
    dic={}
    for e in n:
        if not e in b:
            b[e]=1
        else:
            b[e]+=1
        v=list(dic.values())
        k=list(dic.keys())
        return k[v.index(max(v))]