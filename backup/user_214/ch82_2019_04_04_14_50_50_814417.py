def primeiras_ocorrencias(palavra):
    dic={}
    i=0
    for a in palavra:
        if a in dic:
            dic[a]=dic[a]
            i=i+1
        else:
            dic[a]=i
            i=i+1
    return dic