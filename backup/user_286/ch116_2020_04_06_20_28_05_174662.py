def raiz_quadrada(num):
    sub = 1
    contador =  0
    while num != 0:
        num -= sub
        sub += 2
        contador += 1
    return contador