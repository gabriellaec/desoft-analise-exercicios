def raiz_quadrada(numero):
    if numero == 0:
        return 0
    else: 
        n = 0
        impar = 1
        while impar <= numero:
            numero -= impar
            n += 1
            if numero != 0:
                impar += 2
            else:
                return n
            