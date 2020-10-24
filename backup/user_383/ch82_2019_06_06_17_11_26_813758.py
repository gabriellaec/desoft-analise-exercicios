def primeiras_ocorrencias(palavra):
    dic={}
    i=0
    while i < len(palavra):
        if palavra[i] not in dic:
            dic[palavra[i]] = i
        i+=1
    return dic