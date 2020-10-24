def mais_frequente(lista):
    dic = {}
    c = 0
    for i in lista:
        for a in lista:
            if i == a:
                c += 1
        dic[i] = c
        c = 0
        v=list(dic.values())
        k=list(dic.keys())
        return k[v.index(max(v))]