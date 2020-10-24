def zera_negativos(n):
    x = len(n)
    i = 0
    while i<x:
        
        n[i]<0
        del n[i]
        n[i]=0
        i+=1
        return x