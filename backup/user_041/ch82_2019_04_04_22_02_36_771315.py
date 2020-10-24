def primeiras_ocorrencias(string):
    dic={}
    e=0
    while e<len(string):
        if string[e] not in dic:
            dic[string[e]]=e
        e+=1
    return dic