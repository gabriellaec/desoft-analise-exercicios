def primeiras_ocorrencias(x):
    dic = {}
    c = 0
    for i in range(len(x)):
        if x[i] not in dic:
            dic[x][c] = c
        c +=1
    return dic      