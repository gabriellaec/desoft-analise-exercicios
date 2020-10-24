def primeiras_ocorrencias(palavra):
    a = palavra
    dic = {}
    i = 0
    while i < len(a):
        if a[i] not in dic.keys():
            dic[a[i]] = i
        i += 1
    return dic