def calcula_euler(x, n):
    w= 1
    q= 1
    u= 0
    p= 1
    i= 1
    while i<n:
        q= q * (u+1)
        P= p * x
        w= w + (p/q)
        i+= 1
        U+= 1
    e= w
    return e