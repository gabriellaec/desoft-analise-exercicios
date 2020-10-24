def primeiras_ocorrencias(palavra):
    dic={}
    for e in range(len(palavra)):
        if palavra[e] not in dic:
            dic[palavra[e]]=e
    return dic