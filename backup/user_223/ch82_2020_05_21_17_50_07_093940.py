def primeiras_ocorrencias(s):
    dic={}
    for e in s:
        if e not in dic:
            dic[e]+=1
    return dic