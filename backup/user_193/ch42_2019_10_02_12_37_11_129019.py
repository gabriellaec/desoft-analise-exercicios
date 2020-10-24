def quantos_uns(x):
    x=str(x)
    i=0
    c=0
    while i<len(x):
        if x[i]==str(1):
            c=c+1
        i+=1
    return c