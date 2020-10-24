def primeiras_ocorrencias(palavra):
    dic = {}
    for e in range(len(palavra)):
        letra = palavra [e]
        if e not in dic:
            dic[letra] = e
    return dic
        