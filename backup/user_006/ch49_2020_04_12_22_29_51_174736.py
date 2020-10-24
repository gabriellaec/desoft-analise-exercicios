def inverte_lista(a):
    b=[0]*len(a)
    i=1
    for e in a:
        b[len(a)-i]=e
        i=i+1
    return b