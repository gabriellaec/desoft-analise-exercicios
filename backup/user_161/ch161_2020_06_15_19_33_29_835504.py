
def PiWallis(elementos):
    numerador = 2
    denominador = 1
    contador = 0
    multiplicacao = 1
    while(contador < elementos):
        multiplicacao *= numerador / denominador
        #print("{0}/{1}".format(numerador, denominador))
        if contador%2 == 0:
            denominador += 2
        else:
            numerador += 2
        contador += 1
    return multiplicacao*2