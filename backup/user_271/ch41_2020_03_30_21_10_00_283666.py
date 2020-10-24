def zera_negativos(n):
    num=len(n)
    i=0
    while i<num:
        y=n[i]%2        
        if y!=0:
            n[i]=0
        i+=1
    return n