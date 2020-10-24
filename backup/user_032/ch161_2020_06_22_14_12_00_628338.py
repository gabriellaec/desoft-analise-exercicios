def PiWallis(tamanho):
    contador = 0
    denominador = 1
    numerador = 2
    multiplicacao = 1
    while contador < tamanho:
        multiplicacao *= numerador/denominador
        if contador %2 == 0:
            denominador += 2
        else:
            numerador += 2
        contador += 1
    pi = multiplicacao * 2
    return pi