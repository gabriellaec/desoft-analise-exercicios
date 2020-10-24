def primeiras_ocorrencias(texto):
    dic = {}
    for p, i in enumerate(texto):
        if not i in dic:
            dic[i] = p
    return dic