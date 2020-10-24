def conta_ocorrencias(l):
    dicio={}
    for i in l:
        dicio[i]=l.count(i)
    return dicio