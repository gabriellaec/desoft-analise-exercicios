def zera_negativos(x):
    i=0
    x=[]
    while i<len(x):
        if x[i]<0:
            x[i]=0
            return x
        i+=1