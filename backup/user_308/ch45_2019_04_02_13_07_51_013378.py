def zera_negativos(z):
    i=0
    while i<len(z):
        if z[i]<0:
            z[i]=0
        i+=1
    return z