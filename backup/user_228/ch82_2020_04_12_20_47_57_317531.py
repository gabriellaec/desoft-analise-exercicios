def primeiras_ocorrencias(text):
    dic={}
    i=0
    for e in range(len(text)-1):
        if e not in dic:
            dic[e]=i
            i+=1
        else:
            i+=1
    return dic
            