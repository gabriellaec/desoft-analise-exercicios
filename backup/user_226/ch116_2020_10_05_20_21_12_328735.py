def raiz_quadrada(n):
    i = 1
    raiz = 0
    while n != 0:
        n -= i
        i += 2
        raiz += 1
    return raiz