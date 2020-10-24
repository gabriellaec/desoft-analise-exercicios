def raiz_quadrada(n):
    i = 1
    x = 0
    while n>0:
        n = n-i
        i += 2
        x += 1
    return x