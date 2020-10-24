def primeiras_ocorrencias(x):
    dic = {}
    c = 0
    for i in x:
        if i not in dic:
            dic[i] = c
            c +=1
    return dic