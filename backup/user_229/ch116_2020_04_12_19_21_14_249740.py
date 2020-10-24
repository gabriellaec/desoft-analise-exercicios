def raiz_quadrada(numero):
    if numero == 0:
        return 0
    else: 
        n = 0
        impar = 1
        while impar <= numero:
            x = numero - impar
            n += 1
            impar += 2
        return n
            