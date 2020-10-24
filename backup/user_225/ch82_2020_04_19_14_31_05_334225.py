def primeiras_ocorrencias (string):
    dic = {}
    i = 0
    for e in string:
        if e not in dic:
            dic[e]=i
        i+=1
    return dic