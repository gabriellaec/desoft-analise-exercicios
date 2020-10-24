def primeiras_ocorrencias(n):
    b={}
    for e in n:
        if not e in b:
            b[e]=[e]
    return b
            