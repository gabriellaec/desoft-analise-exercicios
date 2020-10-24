def primeiras_ocorrencias(palavra):
    dic={}
    i=0
    for e in palavra:
        if e not in dic:
            dic[e]=i
        i+=1
    return dic