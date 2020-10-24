def zera_negativos(a):
    i=0
    while i>len(a):
        if a[i]>=0:
            a[i]=a[i]
        else:
            a[i]=0
    return a