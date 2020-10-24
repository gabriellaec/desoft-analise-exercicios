def primeiras_ocorrencias(caractobas):
    dic={}
    for e in range(len(caractobas)):
        if e not in dic:
            dic[caractobas[e]]=e
    return dic