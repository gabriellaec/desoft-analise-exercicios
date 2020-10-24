def mais_frequente(l):
    dicio={}
    for i in l:
        dicio[i]=l.count(i)
    ind=dicio.keys()
    non=dicio.values()
    t=1
    x=ind[0]
    while t<len(ind):
        if x<ind[t]:
            x=ind[t]
        else:
            None
        t+=1
    return (non[ind.index(x)])