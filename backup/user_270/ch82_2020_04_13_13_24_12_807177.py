def primeiras_ocorrencias(s):
    d = {}
    i = 0
    for k in s:
        if not k in d:
            d[k]=i
        i +=1
    return d
        