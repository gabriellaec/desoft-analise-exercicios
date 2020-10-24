def interseccao_valores(d,n):
    l=[]
    for k,v in d.items():
        if v in n.values():
            l.append(v)
    return l