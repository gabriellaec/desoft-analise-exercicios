def arcotangente(x,n):
    i=1 #contador
    y=0
    while i<=n:
        y = y + x**i/i
        i*=2
        y = y - x**i/i
        i+=2
    return y