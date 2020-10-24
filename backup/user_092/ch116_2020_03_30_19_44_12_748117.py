def raiz_quadrada(x):
    s = 1
    c = 0
    y = x - s
    z = 0
    while(y > 0):
        if x > 0:
            z = y - s
            c += 1
        s += 2
    return c