def raiz_quadrada (n):
    c = n
    i = 1
    s = 0
    while c != 0:
        c = c - i
        s += 1
        i += 2
    return s