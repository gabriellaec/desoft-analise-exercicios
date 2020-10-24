def primeiras_ocorrencias(palavra):
    dic = {}
    for e in range(len(palavra)):
        if letra not in dic:
            dic[letra] = e
    return dic
        