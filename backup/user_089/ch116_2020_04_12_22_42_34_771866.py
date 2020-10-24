def raiz_quadrada(n):
    i = 1
    s = []
    if n == 0:
        return 0
    while n != 0:
        n = n - i
        s.append(1)
        i += 2
    p = sum(s)
    return p