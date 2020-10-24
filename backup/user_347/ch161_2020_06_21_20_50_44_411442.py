def PiWallis(n):
    numerador = 2
    denominador = 1
    i = 0
    soma = 1
    while i > n:
        soma *= numerador/denominador
        if i % 2 == 0:
            denominador += 2
            i += 1
        else:
            numerador += 2
            i += 1
    return soma * 2
        
    