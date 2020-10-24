def PiWallis(fatores):
    numerador = 0
    denominador = 1
    produto = 1
    for i in range(fatores):
        if (i+1)%2 == 1:
            numerador += 2
            produto = produto * numerador / denominador
        elif (i+1)%2 == 0:
            denominador += 2
            produto = produto * numerador / denominador
    pi = produto * 2
    return pi