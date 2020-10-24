def zera_negativos(l):
    i=0
    while i<len(l):
        y=l[i]
        if y<0:
            y+=(-y)
            i+=1
        else:
            i+=1
        return y