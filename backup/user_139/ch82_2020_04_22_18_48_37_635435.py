def primeiras_ocorrencias(palavra):
    dic = {}
    for e in range(len(palavra)):
        if e not in dic:
            dic[e] = e
    return dic
        