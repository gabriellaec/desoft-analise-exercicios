def primeiras_ocorrencias(texto):
    dic = {}
    for i in texto:
        if not i in dic:
            dic[i] = index(i)
    return dic