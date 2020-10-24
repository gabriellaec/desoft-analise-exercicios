def primeiras_ocorrencias(string):
    dic = {}
    for i in range(0,len(string)-1):
        if string[i] not in dic:
            dic [string[i]] = i
    return dic