def primeiras_ocorrencias(palavra):
    dic= {}
    for i in range(0, (len(palavra)-1)):
        if plavra[i] not in dic:
            t = palavra[i]
            dic[palavra[i]] = i
    return dic
                   