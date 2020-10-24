def primeiras_ocorrencias(palavra):
    d=[]
    i=0
    while i<len(palavra):
        if palavra[i] not in d:
            d[palavra[i]]=i
        i+=1
    return d