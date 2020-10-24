def raiz_quadrada(n):
    m = 1
    contador = 1
    while m < n:
        if n != 0:
            n = n - m
            contador += 1
            m += 2
    return contador