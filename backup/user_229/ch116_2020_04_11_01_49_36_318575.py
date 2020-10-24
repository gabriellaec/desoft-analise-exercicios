def raiz_quadrada(numero):
    if numero == 0:
        return 0
    else:
        impar = 1
        while impar <= numero:
            x = numero - impar
            if x != 0:
                impar += 2
            else:
                return numero**(1/2)