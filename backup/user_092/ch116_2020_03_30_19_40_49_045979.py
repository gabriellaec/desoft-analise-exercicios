def raiz_quadrada(x):
    s = 1
    c = 0
    y = x
    while(y > 0):
        if x > 0:
            y = x - s
            c += 1
        s += 2
    return c