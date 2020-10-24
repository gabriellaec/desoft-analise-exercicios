def primeiras_ocorrencias(n):
    b={}
    i=0
    for e in n:
        if not e in b:
            b[e]=i
            i+=1
    return b
            