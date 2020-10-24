def interseccao_chaves(d,n):
    l=[]
    for k in d:
        l.append(k)
    for k in n:
        if k not in l:
            l.append(k)
    return l