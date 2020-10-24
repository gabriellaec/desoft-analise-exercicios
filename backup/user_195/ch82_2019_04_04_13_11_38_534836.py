def primeiras_ocorrencias(s):
    D={}
    i=0
    for c in s:
        if c not in D:
            D[c]=i
        i+=1
    return D