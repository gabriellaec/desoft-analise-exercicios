def conta_bigramas(n)
    i=0
    b=[]
    while (i+1)<len(n):
        b.append(n[i]+n[i+1])
        i+=1
    l={}
    for e in b:
        if e in l:
            l[e]+=1
        else:
            l[e]=1
    return l
       
    