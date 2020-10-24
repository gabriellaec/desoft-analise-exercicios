def interseccao_chaves(a,b):
    c=[]
    t=a.keys()
    y=b.keys()
    for i in t:
        for n in y:
            if i==n:
                c.append(t)
    return c