def PiWallis (n):
    contador = 1
    pi = 1
    while contador <= n:
        if contador % 2 =! 0:
            pi *= 2*(((2*contador)/(2*contador-1))
        else:
            pi = ((2*(contador -1))/(2*contador - 1)))
        contador = contador + 1
    return pi