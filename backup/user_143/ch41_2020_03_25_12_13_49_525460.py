def zera_negativos(l):
    i=0
    y=l[i]
    while(i<len(l)-1):
        y=l[i+1]
        if y<0:
            y+=(-y)
            i+=1
        else:
            i+=1
        return y