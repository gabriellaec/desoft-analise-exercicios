def primeiras_ocorrencias(string):
    dic = {}
    c = []
    for i in t:
        c.append(i)
    for i in c:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return(dic)
    