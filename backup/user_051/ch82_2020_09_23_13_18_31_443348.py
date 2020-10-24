def primeiras_ocorrencias(string):
    dic={}
    i=0
    while i<len(string):
        if string[i] not in dic.keys():
            dic[string[i]]=i
        i+=1
    return dic