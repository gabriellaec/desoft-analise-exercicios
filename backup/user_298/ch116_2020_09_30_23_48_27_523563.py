def raiz_quadrada(num):
    t = 1
    w = 1
    if num == 0:
        return 0
    while t < num:
        num = num - t
        t += 2
        w += 1
    return w