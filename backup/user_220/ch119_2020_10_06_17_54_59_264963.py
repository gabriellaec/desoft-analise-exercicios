
def calcula_euler(x,n):
    q = 1
    u = 0
    p = 1
    w = 1 + p
    i = 1
    while i < n:
        q = q * (u+1)
        p = p * x
        w = w + p/q
        i+=1
        u+=1
    e = w **(1/x)
    return e