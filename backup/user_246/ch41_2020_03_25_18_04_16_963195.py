def zera_negativos(x):
    i=len(x)
    t=0
    while t<i:
        if x[t]<0:
            del x[t]
            x.insert(t, 0)
        else:
            None
        t+=1
     	return (x)