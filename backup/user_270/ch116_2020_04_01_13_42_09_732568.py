def raiz_quadrada(n):
    i = 0
    k = n
    x = 1
    while k != 0 :
        k = k - x
        x += 2
        i += 1
    return i