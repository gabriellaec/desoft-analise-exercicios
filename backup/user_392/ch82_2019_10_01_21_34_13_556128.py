def primeiras_ocorrencias(x):
    i = 0
    dic = {}
    for e in x:
        dic[e] = i
        i+=1
    return dic
        