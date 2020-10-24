def primeiras_ocorrencias(palavra):
    dic = {}
    for i in range(len(palavra)):
        if palavra[i] not in dic:
            dic[palavra[i]] = i
    return dic