def monta_mala(l):
    t=len(l)
    i=1
    s=0
    l1=[]
    while i<t:
        if s+l[i]<24:
            s=s+l[i-1]
            l1.append(l[i-1])
            i+=1
        else:
            i+=1
    return l1