def primeiras_ocorrencias (caractere):
    dic = {}
    for e in len(caractobas):
        if caractobas [e] not in dic:
            dic[caractobas[e]] = e
    return dic