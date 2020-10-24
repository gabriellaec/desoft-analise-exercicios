def primeiras_ocorrencias(str):
    dic = {}
    for i in range(len(str)):
        if str[i] not in dic:
            dic[str[i]] = i
            
    return dic
        