def raiz_quadrada(n):
    i = 1
    while n != 0:
        n = n - i
        i += 2
    return i