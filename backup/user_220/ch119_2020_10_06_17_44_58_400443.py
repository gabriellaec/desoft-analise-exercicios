
def calcula_euler(x,n):
    w = 1+x
    q = 1
    u = 1
    p = x
    i = 2
    while i < n:
        q = q * (u+1)
        p = p * x
        w = w + p/q
        i+=1
        u+=1
    e = w **(1/x)
    return e