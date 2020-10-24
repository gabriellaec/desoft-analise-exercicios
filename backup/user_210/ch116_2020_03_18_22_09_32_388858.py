def raiz_quadrada(n):
    cont = 0
    sub = 1
    while n != 0:
        n -= sub
        sub += 2
        cont += 1
    return cont