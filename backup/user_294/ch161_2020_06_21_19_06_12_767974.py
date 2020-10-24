numerador = 2
denominador = 1
pi_meios = 1
def PiWallis (x):
    for i in range(x):
        if numerador %2 == 0 and denominador %2!=0:
            pi_meios *= numerador/denominador
        else:
            pi_meios *= (numerador-1)/(denominador+1)
        numerador += 1
        denominador += 1
        