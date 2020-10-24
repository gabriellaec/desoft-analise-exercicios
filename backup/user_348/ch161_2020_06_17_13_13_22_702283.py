def PiWallis (n):
    contador = 1
    while contador <= n:
        pi = 2*(((2*contador)/(2*contador-1)) * ((2*contador)/(2*contador + 1)))
        contador = contador + 1
    return pi