def primeiras_ocorrencias(palavra):
    dic = {}
    for e in palavra:
        if e not in dic:
            dic[e] = 1
        else:
            dic[e] += 1
    return dic
            
    