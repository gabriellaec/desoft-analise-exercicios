def acha_bigramas(x):
    i=0
    b=[]
    while i<len(x):
        b+=x[i]+x[i+1]
        i+=1
    return x