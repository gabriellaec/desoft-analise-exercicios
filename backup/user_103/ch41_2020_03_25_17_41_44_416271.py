def zera_negativos(n):
    i=0
    num=len(n)
    while i<num:
        if n[i]<0:
            n[1]=0
        i+=1
    return n