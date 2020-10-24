def zera_negativos(l):
    i=0
    while(i<len(l)-1):
        y=l[i]
        if y<0:
            y+=(-y)
        else:
            y=y
    i+=1
    return y