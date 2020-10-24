def conta_ocorrencias(l):
    dic = {}
    for i in l:
        dic[i] = l.count(i)
    return dic



def mais_frequente(l):
    dic = conta_ocorrencias(l)
    maxn = 0
    palavra = 0
    for i, v in dic.items():
        if v > maxn:
            maxn = v
            palavra = i
    return palavra
        