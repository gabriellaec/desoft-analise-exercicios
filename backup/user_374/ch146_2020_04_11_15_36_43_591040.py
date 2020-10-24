def conta_ocorrencias(l1):
    dic = {}
    for i in l1:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic