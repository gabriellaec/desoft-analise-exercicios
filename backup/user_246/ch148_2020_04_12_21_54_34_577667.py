def conta_letras(l):
    p=list(l)
    dicio={}
    for i in p:
        dicio[i]=l.count(i)
    return dicio