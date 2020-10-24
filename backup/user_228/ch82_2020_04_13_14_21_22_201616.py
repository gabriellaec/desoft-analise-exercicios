def primeiras_ocorrencias(text):
    dic={}
    for e in text:
        if e not in dic:
            dic[e]=1
        else:
            dic[e]+=1
    return dic
            