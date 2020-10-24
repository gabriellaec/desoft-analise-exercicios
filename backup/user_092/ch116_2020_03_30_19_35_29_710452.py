def raiz_quadrada(x):
    s = 1
    c = 0
    while(s <= x):
        if x > 0:
            y = x - s
            c += 1
        s += 2
        else:
            break
    return c