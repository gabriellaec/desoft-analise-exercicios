def raiz_quadrada(numero):
    n = 0
    impar = 1
    while impar <= numero:
        x = numero - impar
        n += 1
        impar += 2
    return n
            