def encontra_maximo(ll):
    l1=ll[0]
    l2=ll[1]
    l3=ll[2]
    for i in range(len(l1)):
        l1[i]=abs(l1[i])
        l2[i]=abs(l1[i])
        l3[i]=abs(l1[i])
    m1=max(l1)
    m2=max(l2)
    m3=max(l3)
    ls=[m1,m2,m3]
    m=max(ls)
    return m