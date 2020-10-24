def primeiras_ocorrencias(string):
    dic={}
    for e in string:
        if e not in dic:
            dic[e]=1
        else:
            dic[e]+=1
    return dic
            