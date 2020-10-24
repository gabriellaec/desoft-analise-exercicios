def primeiras_ocorrencias(z):
    i=0
    a=dict()
    for x in z:
        if x in a:
            i+=1
        else:
            a[x]=i
            i+=1
    return a
        