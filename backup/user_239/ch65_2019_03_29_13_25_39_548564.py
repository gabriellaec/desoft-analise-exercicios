def acha_bigramas(x):
    i=0
    b=[]
    s=0
    while i<len(x):
        s=x[i]+x[i+1]
        b.append(s)
        i+=1
    return s