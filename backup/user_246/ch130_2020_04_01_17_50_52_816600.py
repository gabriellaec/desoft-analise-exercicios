def monta_mala(l):
    t=len(l)
    i=0
    s=0
    l1=[]
    while i<t:
        if s<23:
            s=s+l[i]
            l1.append(l[i])
            i+=1
        else:
            i+=1
    return l1