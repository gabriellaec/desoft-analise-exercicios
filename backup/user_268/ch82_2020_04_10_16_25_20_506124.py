def primeiras_ocorrencias(string):
    a = len(string)
    dic={}
    for i in range(a):
        if not string[i] in dic:
            dic[string[i]] = i
    return dic
        
    