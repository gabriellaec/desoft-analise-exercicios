def PiWallis(n):
    numerador,denominador,pi = 2.0, 1.0, 1.0
    for i in range(1,n+1):
        pi*= (numerador / denominador)
        if (i%2) == 1:
            denominador+=2.0
        else:
            numerador+=2.0
    pi*=2.0
    return pi
        
        
    