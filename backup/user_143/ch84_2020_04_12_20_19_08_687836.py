def inverte_dicionario(d1):
    d={}
    l=[]
    for i in d1.values():
        l.append(i)
    i=0
    c=l[i]
    while i<len(l):
        l1=[]
        for j,a in d1.items():
            if a==c:
                l1.append(j)
        d[c]=l1
        i+=1
    return d
            