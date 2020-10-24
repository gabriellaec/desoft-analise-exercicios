def medias_por_inicial (d1):
    l=[]
    d={}
    for i in d1.keys():
        d=i[0]
        l.append(d)
    i=0
    c=0
    while i<len(l):
        e=0
        b=0
        m=0
        c=l[i]
        for a,j in d1.items():
            k=a[0]
            if k==c:
                e+=j
                b+=1
                m=e/b
        d[c]=m
        i+=1
    return d
                