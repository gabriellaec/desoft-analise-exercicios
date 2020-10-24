def raiz_quadrada(x):
    s = 1
    y = 1
    c = 0
    while(y > 0):
        if x > 0:
            y = x - s
            c += 1
        s += 2
    return y