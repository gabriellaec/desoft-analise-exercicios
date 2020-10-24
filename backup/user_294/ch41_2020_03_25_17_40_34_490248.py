def zera_negativos(a):
    i=0
    num=len(a)
    while i<num:
        if a[i]<0:
            a[i]=0
        i=+1
    return a
        