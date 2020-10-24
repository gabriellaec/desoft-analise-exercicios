def arcotangente(x,n):
    i = 1
    s = 2*x
    while i < n:
        s -= ((x**i)/i)
        i += 2
    return s