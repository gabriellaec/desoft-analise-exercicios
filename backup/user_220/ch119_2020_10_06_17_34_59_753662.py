
def calcula_euler(x,n):
    w = 1+x
    q = 1
    p = x
    i = 1
    while i < n:
        q = q * (q+1)
        p = p * x
        w = w + p/q
        i+=1
    e = w **(1/x)
    return e