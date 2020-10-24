def primeiras_ocorrencias(x):
    dic = {}
    for e in x:
        if dic[e]in dic:
        	dic[e] += 1
        else:
            dic[e]=1
    return dic
        