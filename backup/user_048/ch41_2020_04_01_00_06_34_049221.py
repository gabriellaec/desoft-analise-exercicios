def zera_negativos(x):
    t=0
    i=len(x)
    while t<i:
        if x[t]<0:
            del x[t]
            x.insert(t,0)
        t=t+1
        return(x) 