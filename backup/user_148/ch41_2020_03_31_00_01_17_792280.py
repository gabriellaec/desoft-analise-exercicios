def zera_negativos(x):
    
    n = int(len(x))
    i = 0
    
    while i<n:
        if n[i]<0:
            n[i]=0
            i+=1
        else:
            return n