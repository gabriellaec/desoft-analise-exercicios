def conta_ocorrencias(lista):
    dic = {}
    for e in lista:
        if e not in dic:
            dic[e] = 1
        else:
            dic[e] += 1
    return dic