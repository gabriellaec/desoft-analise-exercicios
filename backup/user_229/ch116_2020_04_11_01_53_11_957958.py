def raiz_quadrada(numero):
    n = 0
    impar = 1
    while impar <= numero:
        x = numero - impar
        n += 1
        if x != 0:
            impar += 2
        else:
            return n
            