def raiz_quadrada(num):
    impar = 1
    i = 0
    while num != 0:
        num -= impar
        i += 1
        impar += 2
    return i