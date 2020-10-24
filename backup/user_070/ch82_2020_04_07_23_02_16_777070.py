def primeiras_ocorrencias(x):
    dic = {}
    a = 0
    for i in x:
        if i not in dic:
            dic[i] = a
        a += 1
    return dic