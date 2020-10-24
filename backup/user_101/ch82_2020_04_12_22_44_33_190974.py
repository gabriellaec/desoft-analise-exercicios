def primeiras_ocorrencias(string):
    dic = {}
    for i, e in enumerate(string):
        if e not in dic:
            dic[e] = i
    return dic