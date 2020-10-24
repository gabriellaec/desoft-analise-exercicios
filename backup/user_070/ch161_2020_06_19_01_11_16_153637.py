def PiWallis(x):
    pi_2 = 1
    numerador = 0
    denominador = 1
    for i in range(x):
        if (i+1)%2 == 1:
            numerador += 2
            pi_2 = pi_2 * numerador / denominador
        elif (i+1)%2 == 0:
            denominador += 2
            pi_2 = pi_2 * numerador / denominador
    pi = 2 * pi_2
    return pi