def PiWallis(x):
    numerador = 2
    denominador = 1 
    pimails = 1
    for i in range(x):
        if numerador%2==0 and denominador%2!=0: 
            pimails *= numerador/denominador
        else:
            pimails *= (numerador-1)/(denominador+1)
        numerador+=1
        denominador+=1
    return pimails*2
        