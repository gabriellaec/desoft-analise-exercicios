def zera_negativos(l):
    i=0
    while i<len(l):
        if l[i]<0:
            l[i]+=(-l[i])
            i+=1
        else:
            i+=1
        return l[i]