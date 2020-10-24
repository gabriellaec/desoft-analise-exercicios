def raiz_quadrada(n):
    i = 1
    a = 0
    while i <= n:
        n = n - i
        i += 2
        a += 1
    return a