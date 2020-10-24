def interseccao_valores(a,b):
    c=[]
    t=a.values()
    y=b.values()
    for i in t:
        for n in y:
            if i==n:
                c.append(i)
    return c