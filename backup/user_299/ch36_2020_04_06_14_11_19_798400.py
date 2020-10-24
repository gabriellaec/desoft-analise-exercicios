def fatorial (n):
    i=0
    f=[1]*n
    nf=1
    for i,e in enumerate(f):
        f[i]=i+1
        nf = nf*f[i]
    return nf