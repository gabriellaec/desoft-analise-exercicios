def fact(x):
    t = int(x) - 1
    fatorial = int(x)*t
    while t >= 1:
        fatorial = fatorial*t
    return fatorial