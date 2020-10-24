def raiz_quadrada(x):
    n = x
    i = 1
    cont = 0
    while n > 0:
        n = n - i
        i += 2
        cont += 1
    return cont
