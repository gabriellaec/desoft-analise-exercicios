def fatorial (n):
    i=0
    while i<n:
        f=[1]*n
        f[i+1]=i+1
        nf = nf*f[i+1]
    return nf