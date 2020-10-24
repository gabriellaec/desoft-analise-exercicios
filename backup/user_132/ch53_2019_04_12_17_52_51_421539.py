def inverte_lista(a):
    r=[]
    n = len(a) - 1
    while len(r) < len(a):
        r.append(a[n])
        n = n - 1
    return r
    