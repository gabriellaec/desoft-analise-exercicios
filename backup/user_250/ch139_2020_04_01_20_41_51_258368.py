def arcotangente(x,n):
    i = 1
    c = 0
    arcotg = 0
    while i < n:
        if c%2 == 0:
            arcotg += ((x**i)/i)
            i += 2
            c += 1
        else:
            arcotg += ((x**i)/i)
            i += 2
            c += 1
    return arcotg        