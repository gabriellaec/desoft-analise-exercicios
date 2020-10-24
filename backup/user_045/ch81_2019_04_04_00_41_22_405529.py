def interseccao_valores(d,n):
    l=[]
    for v in d.values():
        if v in n.values():
            l.append(v)
    return l