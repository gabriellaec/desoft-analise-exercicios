def PiWallis(elementos):
    numerador = 2
    denominador = 1
    c= 0
    multiplicacao = 1
    while(c < elementos):
        multiplicacao *= numerador/denominador
        if c % 2 == 0:
            denominador += 2
        else:
            numerador += 2
        c += 1
    return multiplicacao*2