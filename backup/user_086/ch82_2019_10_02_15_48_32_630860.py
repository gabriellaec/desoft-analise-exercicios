def primeiras_ocorrencias(string):
    dic={}
    i=0
    while i<len(string):
        if not string[i] in dic:
            dic[string[i]]=i
    i+=1
    return dic