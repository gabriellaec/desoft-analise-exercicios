def primeiras_ocorrencias(text):
    dic={}
    for e in text:
        if e not in dic:
            dic[e]=i
        else:
            dic[e]+=1
    return dic
            