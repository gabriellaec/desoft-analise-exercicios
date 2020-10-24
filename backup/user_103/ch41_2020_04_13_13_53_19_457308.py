def zera_negativos(n):
    i=0
    num=len(n)
    for i in len(num):
        if n[i]<0:
            n[i]=0
        i+=1
    return n