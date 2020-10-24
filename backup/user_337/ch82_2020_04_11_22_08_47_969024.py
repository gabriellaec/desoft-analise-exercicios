def primeiras_ocorrencias(palavra):
    dic = {}
    a = 0
    for i in palavra:
        if not i in dic:
            dic[i] = a
        a += 1
    return dic