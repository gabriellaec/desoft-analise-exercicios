def raiz_quadrada(num):
    i = 1
    while num > 0:
        num -= i
        i += 2
    return num
        