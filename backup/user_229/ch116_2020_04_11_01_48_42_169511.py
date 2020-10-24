def raiz_quadrada(numero):
    impar = 1
    while impar <= numero:
        x = numero - impar
        if x != 0:
            impar += 2
        else:
            return numero**(1/2)