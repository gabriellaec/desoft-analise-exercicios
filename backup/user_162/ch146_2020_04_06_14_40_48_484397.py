def conta_ocorrencias(l):
    dic = {}
    for i in l:
        dic[i] = l.count(i)
    return dic