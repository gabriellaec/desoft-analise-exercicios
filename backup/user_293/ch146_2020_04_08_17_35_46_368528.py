def conta_ocorrencias(l):
    dic = {}
    for i in l:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic
