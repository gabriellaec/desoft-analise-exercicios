def primeiras_ocorrencias(l):
    dic = {}
    for i in l:
        dic[i] = l.index(i)
    return dic