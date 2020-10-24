def primeiras_ocorrencias(string):
    dic = {}
    i = 0
    for l in string:
        if not l in dic:
            dic[l] = i
    i +=1
    return dic