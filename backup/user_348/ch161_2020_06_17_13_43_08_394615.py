def PiWallis (n):
    contador = 1
    pi = 1
    numerador = 0
    denominador = 1
    while contador <= n:
        if contador % 2 != 0:
            numerador += 2
            pi *= (numerador)/(denominador)
        else:
            denominador += 2
            pi *= (numerador/denominador)
        contador = contador + 1
    return 2 * pi