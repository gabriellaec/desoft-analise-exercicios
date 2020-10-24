def zera_negativos(a):
    b = 0
    while b < len(a):
        if a[b] <= 0:
            a[b] = 0
        b+= 1
    return a