def PiWallis(n):
    numerador=2
    denominador=1
    contador=0
    multiplicacao=1
    while contador<n:
        multiplicacao*=numerador/denominador
        if numerador%2==0:
            numerador+=2
        else:
            denominador+=2
        contador+=1
    return multiplicacao*2