def primeiras_ocorrencias(palavra):
    a = palavra
    dic = {}
    for i in range (len(a)):
        if a[i] not in dic.keys():
            dic[a[i]] = i
    return dic