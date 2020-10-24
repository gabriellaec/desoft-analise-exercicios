def primeiras_ocorrencias(x):
    dic = {}
    c = 0
    for i in range(len(x)):
        if x[i] not in dic:
            dic[x][i] = i
        i +=1
    return dic      