def conta_ocorrencias(lista):
    dic = {}
    c = 0
    for i in lista:
        for a in lista:
            if i == a:
                c += 1
        dic[i] = c
        c = 0
    return dic
def mais_frequente(conta_ocorrencias):
    v=list(dic.values())
    k=list(dic.keys())
    return k[v.index(max(v))]