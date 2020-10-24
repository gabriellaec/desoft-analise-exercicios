def raiz_quadrada(x):
    s = 1
    c = 1
    z = 0
    if x == 0:
        return 0
    y = x - s
    if y == 0:
        return s
    else:
        while(z >= 0):
            z = y - s
            c += 1
            s += 2
        if z == 0:
            return c