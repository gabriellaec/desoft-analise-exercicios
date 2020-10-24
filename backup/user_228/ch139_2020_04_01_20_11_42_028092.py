def arcotangente(x,n):
    i=1
    s=1
    y=0
    while n*2 > i:
        p=s*(x**i)/i
        y=p+y
        i=i+2
        s=s*(-1)
    return y