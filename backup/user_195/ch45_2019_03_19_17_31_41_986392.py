def zera_negativos(L):
    i=0
    while i<len(L):
        if L[i]<0:
            L[i]=0
            i+=1
        else:
            i+=1
    return L