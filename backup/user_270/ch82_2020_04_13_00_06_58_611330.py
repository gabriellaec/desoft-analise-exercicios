def primeiras_ocorrencias(s):
    d = {}
    i = 0
    for k in s:
        d[k]=i
        i +=1
    return d
        