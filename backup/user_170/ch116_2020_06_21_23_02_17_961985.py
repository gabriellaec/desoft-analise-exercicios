def raiz_quadrada(numero):
    n = numero
    c = 0
    i = 1
    while n != 0:
        n -= i
        i += 2
        c += 1
    return c